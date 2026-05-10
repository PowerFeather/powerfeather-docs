#!/usr/bin/env python3
"""Compare SDK source comments/limitations against the rendered docs.

This is intentionally heuristic. It normalizes C++ Doxygen and Markdown enough
to catch missing API facts, numeric ranges, enum names, and limitation details
without requiring identical prose.
"""

import argparse
import re
from pathlib import Path


def strip_doxygen(block: str) -> str:
    block = re.sub(r"^/\*\*|\*/$", "", block.strip(), flags=re.S)
    lines = []
    for line in block.splitlines():
        line = re.sub(r"^\s*\*\s?", "", line)
        line = re.sub(r"@(brief|param(?:\[[^\]]+\])?|return)\b", r"\1", line)
        line = re.sub(r"\\[cap]\s+([A-Za-z0-9_:]+)", r"\1", line)
        line = re.sub(r"\\c\s+([A-Za-z0-9_:().&<>]+)", r"\1", line)
        lines.append(line)
    return "\n".join(lines)


def normalize(text: str) -> str:
    text = re.sub(r"\[[^\]]+\]\([^)]*\)", lambda m: re.match(r"\[([^\]]+)\]", m.group(0)).group(1), text)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = text.replace("::", " ")
    text = text.replace("&", " ")
    text = text.replace("μ", "u").replace("µ", "u")
    text = text.replace("LSb", "LSB")
    text = re.sub(r"\\[A-Za-z]+\s*", "", text)
    text = re.sub(r"[^A-Za-z0-9.%_+\-/]+", " ", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def sentences(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text.strip())
    parts = re.split(r"(?<=[.;:])\s+|(?:\n\s*[-*]\s+)", text)
    return [p.strip(" -*") for p in parts if len(normalize(p)) >= 30]


def signature_key(sig: str) -> str:
    sig = re.sub(r"\[[^\]]+\]\([^)]*\)", lambda m: re.match(r"\[([^\]]+)\]", m.group(0)).group(1), sig)
    sig = re.sub(r"`([^`]*)`", r"\1", sig)
    sig = re.sub(r"\s+", " ", sig.strip())
    sig = sig.replace("&", " &")
    match = re.search(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\(([^)]*)\)", sig)
    if not match:
        return sig

    name, args = match.group(1), match.group(2).strip()
    args = re.sub(r"=.*", "", args)
    args = re.sub(r"\bconst\b|\bvolatile\b", "", args)
    args = re.sub(r"\s+", " ", args).strip()
    arg_types = []
    if args:
        for arg in args.split(","):
            arg = arg.strip()
            arg = re.sub(r"\s*[A-Za-z_][A-Za-z0-9_]*\s*$", "", arg).strip()
            arg = arg.replace(" &", "&").replace("&", "&")
            arg_types.append(arg)
    return f"{name}({','.join(arg_types)})"


def extract_header_methods(path: Path) -> dict[str, str]:
    text = path.read_text()
    out = {}
    comment_pattern = re.compile(r"/\*\*.*?\*/", re.S)
    sig_pattern = re.compile(
        r"^\s*((?:Result|FuelGauge\s*&|BQ2562x\s*&)\s+[A-Za-z_][A-Za-z0-9_]*\s*\([^;{]*\))\s*(?:;|\{)",
        re.M,
    )
    for comment_match in comment_pattern.finditer(text):
        sig_match = sig_pattern.match(text[comment_match.end() :])
        if not sig_match:
            continue
        key = signature_key(sig_match.group(1))
        if key == "getCharger()":
            continue
        out[key] = strip_doxygen(comment_match.group(0))
    return out


def material_tokens(sentence: str) -> set[str]:
    raw = re.sub(r"\\[cap]\s+([A-Za-z0-9_:().&<>]+)", r"\1", sentence)
    raw = re.sub(r"`([^`]*)`", r"\1", raw)
    tokens = set()
    for token in re.findall(
        r"\b(?:Result::)?[A-Z][A-Za-z0-9_]*(?:::[A-Za-z0-9_]+)?\b|"
        r"\b[A-Za-z_][A-Za-z0-9_]*\(\)|"
        r"\b(?:chargeVoltage|ichgTerm|iChgTerm|VINDPM|VBUS|VSQT|VUSB|VDC|ALARM|QON|IBAT_ADC|EN_CHG)\b",
        raw,
    ):
        tokens.add(normalize(token))
    for token in re.findall(
        r"\b\d+(?:\.\d+)?\s*(?:mA|mAh|ms|V|uA|µA|%|mV|LSB)\b|"
        r"\b\d+(?:\.\d+)?-\d+(?:\.\d+)?\s*(?:mA|mAh|V|mV)\b",
        raw,
    ):
        tokens.add(normalize(token))
    for token in re.findall(r"\b[0-9]+\.[0-9]+f\b|\b0x[0-9a-fA-F]+\b", raw):
        tokens.add(normalize(token))
    return {token for token in tokens if token not in {"result", "mainboard", "powerfeather"}}


def extract_md_sections(path: Path) -> dict[str, str]:
    text = path.read_text()
    chunks = re.split(r"(?=^### )", text, flags=re.M)
    out = {}
    for chunk in chunks:
        first = chunk.splitlines()[0] if chunk.splitlines() else ""
        if first.startswith("### "):
            out[signature_key(first)] = chunk
    return out


def extract_result_header(path: Path) -> dict[str, str]:
    text = path.read_text()
    enum = re.search(r"enum class Result\s*\{(?P<body>.*?)\};", text, re.S)
    out = {}
    if enum:
        for name, comment in re.findall(r"([A-Za-z_][A-Za-z0-9_]*)\s*=\s*-?\d+,\s*//\s*(.*)", enum.group("body")):
            out[name] = comment
    return out


def extract_result_md(path: Path) -> dict[str, str]:
    out = {}
    for line in path.read_text().splitlines():
        match = re.match(r"- `([^`]+)`\s+(.*)", line)
        if match:
            out[match.group(1)] = match.group(2)
    return out


def report_missing(header_items: dict[str, str], md_items: dict[str, str], label: str) -> int:
    count = 0
    for key, source in header_items.items():
        target = md_items.get(key)
        if target is None:
            print(f"\n[{label}] missing section: {key}")
            count += 1
            continue
        target_norm = normalize(target)
        missing = []
        for sentence in sentences(source):
            tokens = material_tokens(sentence)
            if not tokens:
                continue
            absent = sorted(token for token in tokens if token not in target_norm)
            if len(absent) >= 2:
                missing.append(f"{sentence}  [missing tokens: {', '.join(absent)}]")
        if missing:
            print(f"\n[{label}] possible content drift: {key}")
            for item in missing:
                print(f"  - {item}")
            count += len(missing)
    return count


def extract_bullets(path: Path) -> list[str]:
    text = path.read_text()
    bullets = []
    current = []
    for line in text.splitlines():
        if re.match(r"^\s*-\s+", line):
            if current:
                bullets.append(" ".join(current))
            current = [re.sub(r"^\s*-\s+", "", line).strip()]
        elif current and (line.startswith("  ") or not line.strip()):
            current.append(line.strip())
        else:
            if current:
                bullets.append(" ".join(current))
                current = []
    if current:
        bullets.append(" ".join(current))
    return bullets


def report_limitations(source_path: Path, md_path: Path) -> int:
    if not source_path.exists():
        return 0
    target_norm = normalize(md_path.read_text())
    count = 0
    for bullet in extract_bullets(source_path):
        tokens = material_tokens(bullet)
        if not tokens:
            continue
        absent = sorted(token for token in tokens if token not in target_norm)
        if absent:
            print("\n[Usage Notes] possible missing limitation:")
            print(f"  - {bullet}")
            print(f"    [missing tokens: {', '.join(absent)}]")
            count += 1
    return count


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--sdk", required=True, help="Path to the powerfeather-sdk checkout")
    parser.add_argument("--docs", required=True, help="Path to this powerfeather-docs checkout")
    args = parser.parse_args()

    sdk = Path(args.sdk)
    docs = Path(args.docs)
    total = 0
    total += report_missing(
        extract_header_methods(sdk / "src/Mainboard/Mainboard.h"),
        extract_md_sections(docs / "docs/sdk/2.x/api/mainboard.md"),
        "Mainboard",
    )
    total += report_missing(
        extract_result_header(sdk / "src/Utils/Result.h"),
        extract_result_md(docs / "docs/sdk/2.x/api/result.md"),
        "Result",
    )
    total += report_limitations(
        sdk.parent / "docs/archive/release-2.0.0/12-supported-usage-limitations.md",
        docs / "docs/sdk/usage-notes.md",
    )

    if total == 0:
        print("No obvious missing API/usage-note source content found.")
    else:
        print(f"\nFound {total} possible missing/drifted item(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
