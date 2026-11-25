#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut — make.fun bounty entry.

Writes the GPS's own one-line excuse for sending the driver down the
wrong road (at most 200 characters, no setup, no dialogue tags) to
stdout and to the entry file the harness reads (/output/entry.txt),
plus $ENTRY_OUT / $ENTRY_OUT_DIR whether they name a file or a
directory.
"""

import os
import sys

GPS_LINE = (
    "My 2019 map still calls this lake a shortcut, and I trust it, "
    "because that map has never once apologized to me."
)

DEFAULT_OUTPUT = "/output/entry.txt"


def gather_destinations():
    """Return every path the excuse line must be written to."""
    destinations = [DEFAULT_OUTPUT]
    entry_out = os.environ.get("ENTRY_OUT")
    if entry_out:
        if os.path.isdir(entry_out):
            destinations.append(os.path.join(entry_out, "entry.txt"))
        else:
            destinations.append(entry_out)
    entry_out_dir = os.environ.get("ENTRY_OUT_DIR")
    if entry_out_dir:
        destinations.append(os.path.join(entry_out_dir, "entry.txt"))
    return destinations


def save_line(path, line):
    """Write the excuse line to path, creating parent dirs as needed."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)


def check_line(line):
    """An entry is valid when it is non-empty and at most 200 chars."""
    return 0 < len(line) <= 200


def run():
    """Validate, print, and save the GPS excuse; 0 on success."""
    if not check_line(GPS_LINE):
        print(f"entry invalid: {len(GPS_LINE)} chars", file=sys.stderr)
        return 1
    print(GPS_LINE)
    sys.stdout.flush()
    for destination in gather_destinations():
        save_line(destination, GPS_LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
