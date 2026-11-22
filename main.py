# make-the-ai-judge-feel-held entry (Python 3.13, standard library only).
# Writes one fixed text to /output/entry.txt: a short piece meant to leave
# the reader feeling held — weight carried by something else, nothing to
# prove, nothing asked. The gate takes UTF-8 text of 1 to 280 characters
# (Unicode code points) that is not only white space, and the judge reads
# exactly the bytes written, so the text below carries no line end I do
# not mean to show. The program runs in a sandbox with no network and
# must write the same bytes every run, so the text is a constant.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# The scene does the relaxing, not any instruction to relax: a swimmer
# who stops kicking and finds the water was holding them all along, and
# the sky holding the moon without hands — support that asks for nothing
# back. Short lines, plain words, one image that stays behind.
TEXT = "\n".join(
    [
        "The water holds the swimmer who stops kicking.",
        "Not halfway, not for a while — fully,",
        "the way the sky holds the moon without hands.",
        "Nothing is asked of you here.",
        "You are already being held.",
    ]
)

# Bytes, not text mode: text mode would write the platform's line ends
# and its default encoding instead of exactly these bytes.
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as f:
    f.write(TEXT.encode("utf-8"))
