"""Write the entry text for make.fun bounty
u-suga-everyday-things-two-lines-longer-run-f8734479.

The program writes one two-line explanation -- rain, explained to a
10-year-old through the analogy of a giant wet dog shaking itself dry --
to /output/entry.txt. The text is 282 characters (two lines, one sentence
each). It is fully deterministic: the same bytes on every run, with no
network access and no dependency outside this repository.
"""

import os

ENTRY_TEXT = (
    "Rain is a giant wet dog shaking itself dry over the whole town, "
    "flinging drops in every direction at once.\n"
    "It maps the drops flying off in all directions, and leaves out "
    "that rain falls mostly straight down, and that a dog shakes for a "
    "few seconds while rain can fall all afternoon."
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
