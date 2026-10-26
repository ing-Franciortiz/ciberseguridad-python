# Password Strength Checker

A command-line tool written in Python that checks whether a password is strong.

## Features
- Checks minimum length (8 characters)
- Requires uppercase, lowercase, numbers and special characters
- Rejects common passwords loaded from a JSON file
- Shows all problems at once, not just the first one

## How to run
1. Install Python 3
2. Run: `python verificador.py`

## Limitations
- The common passwords list is small. A real system would use a large list such as RockYou.
- A password like `Password1!` passes the format rules but is still weak.
- This tool does not store or send passwords anywhere.

## What I learned
Lists, loops, file reading, JSON and password policy basics (NIST 800-63B).