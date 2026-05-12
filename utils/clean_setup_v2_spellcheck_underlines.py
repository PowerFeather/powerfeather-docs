#!/usr/bin/env python3
"""Remove red spellcheck squiggles from setup_v2 Arduino IDE search screenshots."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

from PIL import Image


TARGETS = [
    "install_board_support.png",
    "install_powerfeather_sdk.png",
]


@dataclass(frozen=True)
class Result:
    path: Path
    search_box: tuple[int, int, int, int] | None
    changed_pixels: int
    wrote_file: bool


def is_cyan_border(red: int, green: int, blue: int, alpha: int) -> bool:
    return (
        alpha > 0
        and 70 <= red <= 170
        and 160 <= green <= 235
        and 160 <= blue <= 235
        and green - red > 35
        and blue - red > 35
    )


def is_red_squiggle(red: int, green: int, blue: int, alpha: int) -> bool:
    is_high_luminance_warm_pixel = red >= 220 and (red - green > 4 or red - blue > 4 or blue < 245)
    return (
        alpha > 0
        and is_high_luminance_warm_pixel
    )


def horizontal_runs(values: list[int]) -> list[tuple[int, int]]:
    if not values:
        return []

    runs = []
    start = values[0]
    previous = values[0]
    for value in values[1:]:
        if value == previous + 1:
            previous = value
            continue
        runs.append((start, previous + 1))
        start = previous = value
    runs.append((start, previous + 1))
    return runs


def find_search_box(image: Image.Image) -> tuple[int, int, int, int] | None:
    """Find the first long cyan-outlined input in the upper-left IDE side panel."""
    candidates: list[tuple[int, int, int]] = []
    scan_width = min(320, image.width)
    scan_height = min(240, image.height)

    for y in range(scan_height):
        xs = [
            x
            for x in range(scan_width)
            if is_cyan_border(*image.getpixel((x, y)))
        ]
        for left, right in horizontal_runs(xs):
            if right - left >= 120:
                candidates.append((y, left, right))

    for top, left, right in candidates:
        for bottom, bottom_left, bottom_right in candidates:
            if 18 <= bottom - top <= 35 and abs(bottom_left - left) <= 3 and abs(bottom_right - right) <= 3:
                return (min(left, bottom_left), top, max(right, bottom_right), bottom + 1)

    return None


def clean_image(path: Path, dry_run: bool) -> Result:
    original = Image.open(path).convert("RGBA")
    image = original.copy()
    search_box = find_search_box(image)
    if search_box is None:
        return Result(path=path, search_box=None, changed_pixels=0, wrote_file=False)

    left, top, right, bottom = search_box
    pixels = image.load()
    changed = 0
    # The spellcheck squiggle sits in the bottom of the search field. Restrict
    # cleanup to that underline band so LCD/subpixel antialiasing in the typed
    # text is preserved.
    underline_top = max(top + 1, bottom - 11)
    underline_bottom = max(underline_top, bottom - 2)
    for y in range(underline_top, underline_bottom):
        for x in range(left + 1, right - 1):
            red, green, blue, alpha = pixels[x, y]
            if is_red_squiggle(red, green, blue, alpha):
                pixels[x, y] = (255, 255, 255, alpha)
                changed += 1

    wrote = False
    if changed and not dry_run:
        image.save(path)
        wrote = True

    return Result(path=path, search_box=search_box, changed_pixels=changed, wrote_file=wrote)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--assets-dir",
        default="docs/sdk/assets/setup_v2",
        type=Path,
        help="Directory containing setup_v2 PNG screenshots.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Report changes without writing files.")
    args = parser.parse_args()

    missing = [args.assets_dir / name for name in TARGETS if not (args.assets_dir / name).is_file()]
    if missing:
        for path in missing:
            print(f"missing: {path}")
        return 1

    for name in TARGETS:
        result = clean_image(args.assets_dir / name, dry_run=args.dry_run)
        if result.search_box is None:
            print(f"skipped: {result.path} search box not found")
            continue
        action = "would update" if args.dry_run and result.changed_pixels else "updated" if result.wrote_file else "unchanged"
        print(f"{action}: {result.path} search_box={result.search_box} red_pixels={result.changed_pixels}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
