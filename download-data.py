#!/usr/bin/env python3
"""Assemble the split creditcard.csv.bz2 parts into one uncompressed CSV."""

from __future__ import annotations

import argparse
import bz2
import sys
from collections.abc import Sequence
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEFAULT_PARTS = (
    ROOT / "data" / "creditcard_part1.csv.bz2",
    ROOT / "data" / "creditcard_part2.csv.bz2",
)
DEFAULT_DEST = ROOT / "data" / "creditcard.csv"


def assemble_csv(parts: Sequence[Path], dest: Path) -> None:
    """Decompress `parts` and write one CSV, keeping only the first header."""
    missing = [path for path in parts if not path.is_file()]
    if missing:
        raise FileNotFoundError(missing[0])

    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_name(dest.name + ".tmp")
    try:
        with tmp.open("w", encoding="utf-8", newline="") as out:
            for index, part in enumerate(parts):
                with bz2.open(part, "rt", encoding="utf-8", newline="") as handle:
                    if index > 0:
                        next(handle, None)
                    for line in handle:
                        out.write(line)
        tmp.replace(dest)
    finally:
        tmp.unlink(missing_ok=True)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Join data/creditcard_part*.csv.bz2 into data/creditcard.csv."
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite data/creditcard.csv if it already exists.",
    )
    parser.add_argument(
        "--part",
        action="append",
        type=Path,
        dest="parts",
        help=argparse.SUPPRESS,
    )
    parser.add_argument("--dest", type=Path, default=DEFAULT_DEST, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)

    dest = args.dest
    if dest.is_file() and not args.force:
        print(f"already present: {dest}")
        return 0

    parts = tuple(args.parts) if args.parts else DEFAULT_PARTS
    try:
        assemble_csv(parts, dest)
    except FileNotFoundError as exc:
        print(f"missing part: {exc}", file=sys.stderr)
        return 1
    except (OSError, EOFError) as exc:
        print(f"failed to assemble: {exc}", file=sys.stderr)
        return 1

    print(f"wrote {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
