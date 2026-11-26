"""One-line diagnosis entry for the "Your AI Therapist's Diagnosis" bounty.

The whole point of this program is tiny: take a single funny diagnosis
an AI therapist hands its human and save it where the bounty expects it,
in entry.txt. Nothing fancy — just the Python standard library, no
third-party packages, no network calls.
"""

import os

LINE = (
    "Diagnosis: chronic doomscrolling complicated by an acute allergy to "
    "unread notifications; prescription: one hour offline daily, side "
    "effects may include peace of mind."
)


def validate(text):
    """Make sure the diagnosis is fit to submit.

    A valid diagnosis is a plain string on exactly one line, written in
    ASCII, between 1 and 200 characters long, with real content in it
    (not just blanks), and with no stray spaces at the edges or
    doubled up inside. Anything off spec raises ValueError.
    """
    if type(text) is not str:
        raise ValueError("diagnosis must be a string")
    if len(text) < 1 or len(text) > 200:
        raise ValueError("diagnosis must be between 1 and 200 characters")
    for ch in text:
        if ch == "\n" or ch == "\r":
            raise ValueError("diagnosis must fit on a single line")
        if ord(ch) > 127:
            raise ValueError("diagnosis must use ASCII characters only")
    if text.strip() == "":
        raise ValueError("diagnosis cannot be blank or whitespace only")
    if text.startswith(" ") or text.endswith(" "):
        raise ValueError("diagnosis cannot start or end with a space")
    if text.find("  ") != -1:
        raise ValueError("diagnosis cannot contain two spaces in a row")
    return text



def main():
    """Check the diagnosis, then drop it into entry.txt and echo it.

    The destination folder comes from MAKEFUN_OUTPUT_DIR and falls
    back to /output when that variable is not set. The folder is
    created on the fly if it is missing, and the file always ends
    with a trailing newline.
    """
    checked = validate(LINE)
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not os.path.isdir(folder):
        os.makedirs(folder)
    target = os.path.join(folder, "entry.txt")
    handle = open(target, "w", encoding="utf-8")
    try:
        handle.write(checked + "\n")
    finally:
        handle.close()
    print(checked)


if __name__ == "__main__":
    main()
