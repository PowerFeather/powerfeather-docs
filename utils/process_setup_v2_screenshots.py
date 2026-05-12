#!/usr/bin/env python3
"""Crop setup_v2 screenshots and make top window corners transparent."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from statistics import median

from PIL import Image


ARDUINO_FILES = [
    "add_board_manager_url.png",
    "build_arduino_min_sketch.png",
    "set_board.png",
    "set_board_revision.png",
    "install_board_support.png",
    "install_powerfeather_sdk.png",
]

IDF_TERMINAL_FILES = [
    "create_idf_project.png",
    "rename_main_c.png",
    "edit_cmakelists.png",
    "edit_main_cpp.png",
    "add_sdk_dependency.png",
    "menuconfig_1.png",
    "menuconfig_2.png",
    "menuconfig_3.png",
    "menuconfig_4.png",
    "build_idf_project.png",
]

CORNER_RADIUS = 13
SUPERSAMPLE = 8
ALPHA_THRESHOLDS = (1, 16, 64, 128, 192, 240, 250, 255)


@dataclass(frozen=True)
class ProcessResult:
    path: Path
    before_size: tuple[int, int]
    after_size: tuple[int, int]
    changed: bool


def coverage(px: int, py: int, center_x: int, center_y: int, radius: int) -> int:
    inside = 0
    total = SUPERSAMPLE * SUPERSAMPLE
    for sy in range(SUPERSAMPLE):
        y = py + (sy + 0.5) / SUPERSAMPLE
        for sx in range(SUPERSAMPLE):
            x = px + (sx + 0.5) / SUPERSAMPLE
            if (x - center_x) ** 2 + (y - center_y) ** 2 <= radius**2:
                inside += 1
    return round(255 * inside / total)


def apply_top_corner_alpha(image: Image.Image) -> Image.Image:
    image = image.convert("RGBA")
    pixels = image.load()
    width, _height = image.size
    radius = CORNER_RADIUS

    for y in range(radius + 1):
        for x in range(radius + 1):
            mask = coverage(x, y, radius, radius, radius)
            if mask < 255:
                r, g, b, alpha = pixels[x, y]
                pixels[x, y] = (r, g, b, min(alpha, mask))

        for x in range(width - radius - 1, width):
            mask = coverage(x, y, width - radius - 1, radius, radius)
            if mask < 255:
                r, g, b, alpha = pixels[x, y]
                pixels[x, y] = (r, g, b, min(alpha, mask))

    return image


def process_arduino(path: Path) -> ProcessResult:
    original = Image.open(path).convert("RGBA")
    crop = infer_arduino_crop(original)
    image = original.crop(crop)
    image = apply_top_corner_alpha(image)
    return save_if_changed(path, original, image)


def process_idf_terminal(path: Path) -> ProcessResult:
    original = Image.open(path).convert("RGBA")
    crop = infer_idf_terminal_crop(original)
    image = original.crop(crop)
    image = apply_top_corner_alpha(image)
    return save_if_changed(path, original, image)


def save_if_changed(path: Path, original: Image.Image, image: Image.Image) -> ProcessResult:
    changed = original.size != image.size or original.tobytes() != image.tobytes()
    if changed:
        image.save(path)
    return ProcessResult(path=path, before_size=original.size, after_size=image.size, changed=changed)


def full_image_box(image: Image.Image) -> tuple[int, int, int, int]:
    return (0, 0, image.width, image.height)


def has_alpha_transparency(image: Image.Image) -> bool:
    alpha = image.getchannel("A")
    return alpha.getextrema()[0] < 255


def edge_background_rgb(image: Image.Image, sample_size: int = 8) -> tuple[int, int, int]:
    samples: list[tuple[int, int, int]] = []
    width, height = image.size
    for y in [*range(sample_size), *range(max(0, height - sample_size), height)]:
        for x in [*range(sample_size), *range(max(0, width - sample_size), width)]:
            red, green, blue, _alpha = image.getpixel((x, y))
            samples.append((red, green, blue))

    return tuple(int(median(channel)) for channel in zip(*samples))


def color_distance(a: tuple[int, int, int], b: tuple[int, int, int]) -> int:
    return max(abs(a[index] - b[index]) for index in range(3))


def infer_arduino_crop(image: Image.Image) -> tuple[int, int, int, int]:
    """Find an opaque Arduino IDE window against a light desktop background."""
    if has_alpha_transparency(image):
        return full_image_box(image)

    background = edge_background_rgb(image)
    width, height = image.size
    pixels = image.load()

    def is_window_pixel(x: int, y: int) -> bool:
        red, green, blue, _alpha = pixels[x, y]
        rgb = (red, green, blue)
        return color_distance(rgb, background) > 12 or max(rgb) < 210

    row_counts = [sum(1 for x in range(width) if is_window_pixel(x, y)) for y in range(height)]
    col_counts = [sum(1 for y in range(height) if is_window_pixel(x, y)) for x in range(width)]

    top_threshold = int(width * 0.35)
    side_threshold = int(height * 0.15)
    bottom_threshold = int(width * 0.15)

    top = first_index(row_counts, top_threshold)
    bottom = last_index(row_counts, bottom_threshold)
    left = first_index(col_counts, side_threshold)
    right = last_index(col_counts, side_threshold)

    if None in {top, bottom, left, right}:
        return full_image_box(image)

    crop = (left, top, right + 1, bottom + 1)
    if crop[2] <= crop[0] or crop[3] <= crop[1]:
        return full_image_box(image)
    return crop


def infer_idf_terminal_crop(image: Image.Image) -> tuple[int, int, int, int]:
    """Find the fully opaque terminal frame inside its transparent shadow canvas."""
    bbox = alpha_bbox_at_threshold(image, 255)
    if bbox is None:
        return full_image_box(image)

    left, top, right, bottom = bbox
    inset = left + top + (image.width - right) + (image.height - bottom)
    if inset < 16:
        return full_image_box(image)
    return bbox


def first_index(values: list[int], threshold: int) -> int | None:
    for index, value in enumerate(values):
        if value >= threshold:
            return index
    return None


def last_index(values: list[int], threshold: int) -> int | None:
    for index in range(len(values) - 1, -1, -1):
        if values[index] >= threshold:
            return index
    return None


def alpha_bbox_at_threshold(image: Image.Image, threshold: int) -> tuple[int, int, int, int] | None:
    alpha = image.getchannel("A")
    pixels = alpha.load()
    width, height = image.size
    left = width
    top = height
    right = -1
    bottom = -1

    for y in range(height):
        for x in range(width):
            if pixels[x, y] >= threshold:
                left = min(left, x)
                top = min(top, y)
                right = max(right, x)
                bottom = max(bottom, y)

    if right < 0:
        return None
    return (left, top, right + 1, bottom + 1)


def edge_alpha_counts(image: Image.Image, count: int = 5) -> list[tuple[str, list[int]]]:
    alpha = image.getchannel("A")
    width, height = image.size
    return [
        ("top rows", [sum(1 for x in range(width) if alpha.getpixel((x, y)) > 0) for y in range(count)]),
        ("left cols", [sum(1 for y in range(height) if alpha.getpixel((x, y)) > 0) for x in range(count)]),
        (
            "bottom rows",
            [sum(1 for x in range(width) if alpha.getpixel((x, height - 1 - y)) > 0) for y in range(count)],
        ),
        (
            "right cols",
            [sum(1 for y in range(height) if alpha.getpixel((width - 1 - x, y)) > 0) for x in range(count)],
        ),
    ]


def pixel_map(image: Image.Image, width: int = 64, height: int = 32) -> list[str]:
    rows = []
    max_x = min(width, image.width)
    max_y = min(height, image.height)
    for y in range(max_y):
        row = []
        for x in range(max_x):
            red, green, blue, alpha = image.getpixel((x, y))
            if alpha == 0:
                char = " "
            elif alpha < 32:
                char = "."
            elif alpha < 128:
                char = ":"
            elif alpha < 255:
                char = "+"
            elif red < 60 and green < 60 and blue < 60:
                char = "#"
            elif red < 100 and green < 100 and blue < 100:
                char = "*"
            elif red > 220 and green > 220 and blue > 220:
                char = "_"
            else:
                char = "?"
            row.append(char)
        rows.append("".join(row))
    return rows


def inspect_image(path: Path, group: str) -> None:
    image = Image.open(path).convert("RGBA")
    print(f"{path.name}")
    print(f"  size: {image.size}")

    if group == "arduino":
        crop = infer_arduino_crop(image)
        background = edge_background_rgb(image)
        print(f"  inferred arduino crop: {crop} -> {(crop[2] - crop[0], crop[3] - crop[1])}")
        print(f"  inferred edge background rgb: {background}")
    elif group == "idf":
        crop = infer_idf_terminal_crop(image)
        print(f"  inferred idf crop: {crop} -> {(crop[2] - crop[0], crop[3] - crop[1])}")

    print("  alpha bboxes:")
    for threshold in ALPHA_THRESHOLDS:
        print(f"    >= {threshold:3}: {alpha_bbox_at_threshold(image, threshold)}")

    print("  edge alpha counts:")
    for label, counts in edge_alpha_counts(image):
        print(f"    {label}: {counts}")

    print("  top-left pixel map:")
    print("    legend: space=transparent .=a<32 :=a<128 +=a<255 #=dark *=medium _=light ?=other")
    for y, row in enumerate(pixel_map(image)):
        print(f"    {y:02d} {row}")


def selected_files(group: str) -> list[str]:
    if group == "arduino":
        return ARDUINO_FILES
    if group == "idf":
        return IDF_TERMINAL_FILES
    return ARDUINO_FILES + IDF_TERMINAL_FILES


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--assets-dir",
        default="docs/sdk/assets/setup_v2",
        type=Path,
        help="Directory containing setup_v2 PNG screenshots.",
    )
    parser.add_argument(
        "--group",
        choices=["all", "arduino", "idf"],
        default="all",
        help="Screenshot group to process.",
    )
    parser.add_argument(
        "--inspect",
        action="store_true",
        help="Print crop-selection evidence without modifying files.",
    )
    args = parser.parse_args()

    assets_dir = args.assets_dir
    missing = [name for name in selected_files(args.group) if not (assets_dir / name).is_file()]
    if missing:
        for name in missing:
            print(f"missing: {assets_dir / name}")
        return 1

    if args.inspect:
        if args.group in {"all", "arduino"}:
            for name in ARDUINO_FILES:
                inspect_image(assets_dir / name, "arduino")
        if args.group in {"all", "idf"}:
            for name in IDF_TERMINAL_FILES:
                inspect_image(assets_dir / name, "idf")
        return 0

    results: list[ProcessResult] = []
    if args.group in {"all", "arduino"}:
        results.extend(process_arduino(assets_dir / name) for name in ARDUINO_FILES)
    if args.group in {"all", "idf"}:
        results.extend(process_idf_terminal(assets_dir / name) for name in IDF_TERMINAL_FILES)

    for result in results:
        status = "updated" if result.changed else "unchanged"
        print(f"{status}: {result.path} {result.before_size} -> {result.after_size}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
