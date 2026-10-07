#!/usr/bin/env python3
"""Extract .l5x files from .p5x archives."""

from __future__ import annotations

import os
import shutil
import sys
import zipfile
from pathlib import Path

WINDOWS_DESKTOP_HINT = "Desktop/p5x_test"


def find_input_output_dirs() -> tuple[Path, Path]:
    """Resolve default input/output folders.

    By default this script expects:
      <script folder>/p5x_test  -> contains .p5x files
      <script folder>/l5x_output -> where .l5x files are written

    If the script is run from a Windows desktop layout, the path is also
    supported via the documented Desktop folder structure.
    """
    script_dir = Path(__file__).resolve().parent
    input_dir = script_dir / "p5x_test"
    output_dir = script_dir / "l5x_output"

    if not input_dir.exists():
        user_profile = os.environ.get("USERPROFILE")
        if user_profile:
            alt_input = Path(user_profile) / "Desktop" / "p5x_test"
            alt_output = Path(user_profile) / "Desktop" / "l5x_output"
            if alt_input.exists():
                input_dir = alt_input
                output_dir = alt_output

    return input_dir, output_dir


def extract_l5x_from_p5x(p5x_path: Path, output_dir: Path) -> list[Path]:
    """Extract .l5x files from a single .p5x archive."""
    extracted: list[Path] = []
    source_output_dir = output_dir / p5x_path.stem
    source_output_dir.mkdir(parents=True, exist_ok=True)

    try:
        with zipfile.ZipFile(p5x_path, "r") as archive:
            members = [name for name in archive.namelist() if name.lower().endswith(".l5x")]

            if not members:
                print(f"No L5X files found inside: {p5x_path.name}")
                return extracted

            for member_name in members:
                target_name = Path(member_name).name
                target_path = source_output_dir / target_name
                with archive.open(member_name, "r") as src, open(target_path, "wb") as dst:
                    shutil.copyfileobj(src, dst)
                extracted.append(target_path)
                print(f"Extracted: {target_path}")
    except zipfile.BadZipFile as exc:
        print(f"BadZipFile in {p5x_path.name}: {exc}")
    except Exception as exc:  # pragma: no cover - defensive catch
        print(f"Error processing {p5x_path.name}: {exc}")

    return extracted


def main() -> int:
    input_dir, output_dir = find_input_output_dirs()
    output_dir.mkdir(parents=True, exist_ok=True)

    print("P5X TO L5X CONVERTER")
    print(f"Input folder: {input_dir}")
    print(f"Output folder: {output_dir}")

    if not input_dir.exists():
        print(f"Folder not found: {input_dir}")
        print(f"Create '{WINDOWS_DESKTOP_HINT}' and place your .p5x files there.")
        return 1

    p5x_files = sorted(input_dir.glob("*.p5x"))
    if not p5x_files:
        print(f"No .p5x files found in {input_dir}")
        return 1

    print(f"Found {len(p5x_files)} P5X file(s)")

    total_extracted = 0
    for p5x_path in p5x_files:
        files = extract_l5x_from_p5x(p5x_path, output_dir)
        total_extracted += len(files)

    print(f"EXTRACTION COMPLETE")
    print(f"Extracted {total_extracted} L5X file(s) to {output_dir}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_dir = Path(sys.argv[1]).resolve()
        output_dir = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else input_dir.parent / "l5x_output"
        print("Using custom input/output directories.")
        print(f"Input folder: {input_dir}")
        print(f"Output folder: {output_dir}")
        if not input_dir.exists():
            print(f"Folder not found: {input_dir}")
            raise SystemExit(1)

        output_dir.mkdir(parents=True, exist_ok=True)
        p5x_files = sorted(input_dir.glob("*.p5x"))
        if not p5x_files:
            print(f"No .p5x files found in {input_dir}")
            raise SystemExit(1)

        total_extracted = 0
        for p5x_path in p5x_files:
            total_extracted += len(extract_l5x_from_p5x(p5x_path, output_dir))

        print(f"EXTRACTION COMPLETE")
        print(f"Extracted {total_extracted} L5X file(s) to {output_dir}")
        raise SystemExit(0)

    raise SystemExit(main())
