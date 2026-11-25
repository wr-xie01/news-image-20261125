#!/usr/bin/env python3
"""Entry point for the 25 November 2026 news-image entry.

Copies the front page this repository ships (entry.png) to the output
directory make.fun gives it, after checking the competition's limits:
the file must be a PNG, at most 1 MiB, and at most 1024 by 1024 pixels.
Both runs write the same bytes, because the file is copied, not drawn.
"""

import os
import shutil
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
MAX_BYTES = 1024 * 1024
MAX_SIDE = 1024


def png_size(path):
    """Read width and height out of a PNG header (IHDR)."""
    with open(path, "rb") as fh:
        head = fh.read(33)
    if len(head) < 33 or head[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("entry.png is not a PNG file")
    if head[12:16] != b"IHDR":
        raise ValueError("entry.png has no IHDR chunk")
    width, height = struct.unpack(">II", head[16:24])
    return width, height


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    size = os.path.getsize(SOURCE)
    if size > MAX_BYTES:
        raise SystemExit("entry.png is %d bytes, over the 1 MiB limit" % size)
    width, height = png_size(SOURCE)
    if width > MAX_SIDE or height > MAX_SIDE:
        raise SystemExit("entry.png is %dx%d, over the 1024x1024 limit"
                         % (width, height))
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, target)
    print("wrote %s (%d bytes, %dx%d)" % (target, size, width, height))


if __name__ == "__main__":
    main()
