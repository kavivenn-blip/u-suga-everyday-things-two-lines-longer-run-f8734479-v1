"""Write the entry text for make.fun bounty
u-suga-everyday-things-two-lines-longer-run-f8734479.

The program writes one two-line explanation -- a toaster, explained to a
10-year-old through the analogy of a hairdryer that forgot the hair and
learned to brown bread -- to /output/entry.txt. The text is 253 characters
(two lines, one sentence each). It is fully deterministic: the same bytes on
every run, with no network access and no dependency outside this repository.

PUTARAN 1 (perbaikan B1): teks ini menggantikan teks PUTARAN 0 (rain as a giant
wet dog, 282 karakter). Kendaraan "wet dog" terbukti dipakai 5 judul feed,
sehingga pemenang turnamen ulang adalah F4x (toaster/hairdryer perluasan).
"""

import os

ENTRY_TEXT = (
    "A toaster is a hairdryer that forgot the hair and learned to brown "
    "bread for breakfast instead.\n"
    "It maps the hot wires inside, and leaves out the blowing air: a "
    "toaster heats bread without any fan at all \u2014 and nobody ever dries "
    "their hair with a toaster."
)

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Self-check against the bounty gate: UTF-8 text of 1 to 400
    # characters, not only white space. Fail loudly instead of
    # writing an entry the sealed scorer would refuse.
    if not 1 <= len(ENTRY_TEXT) <= 400 or not ENTRY_TEXT.strip():
        raise SystemExit("entry text fails the 1-400 character gate")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
