"""makefun-haunted-sign: one funny sign for a haunted server room door.

The program writes a single line to entry.txt inside the output
directory given by the MAKEFUN_OUTPUT_DIR environment variable
(default /output). It uses only the Python standard library, makes no
network calls, and is fully deterministic: every run writes the same
bytes.
"""

import os
import shutil

SIGN = "DO NOT UNPLUG THE GHOST. IT IS THE ONLY ONE WHO REMEMBERS THE WIFI PASSWORD."


def main() -> None:
    # The gate requires 1 to 120 characters of non-whitespace text.
    if not 1 <= len(SIGN) <= 120 or not SIGN.strip():
        raise ValueError("sign must be 1 to 120 characters of text")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    # Clear only the contents of the output directory, never the
    # directory itself, and write nothing outside it.
    for name in os.listdir(output_dir):
        path = os.path.join(output_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(SIGN)


if __name__ == "__main__":
    main()
