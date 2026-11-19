"""Deliver the finished front-page image to the grader's output folder.

The image itself ships in this repository as entry.png, already drawn
at 1024x1024. This program just moves those bytes to where the grader
looks: the directory named by MAKEFUN_OUTPUT_DIR, or /output when the
variable is absent. It uses only the standard library, touches no
network, and copies the file byte for byte, so repeated runs produce
identical output. A missing source image or a short copy is an error,
not a silent partial run.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
IMAGE = HERE / "entry.png"
DEST_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    if not IMAGE.is_file():
        raise FileNotFoundError(f"front-page image not found: {IMAGE}")
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    target = DEST_DIR / "entry.png"
    shutil.copyfile(IMAGE, target)
    got = target.stat().st_size
    want = IMAGE.stat().st_size
    if got != want:
        raise IOError(f"copied {got} bytes, expected {want}")


if __name__ == "__main__":
    main()
