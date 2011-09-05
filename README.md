
# About

This is a simple Python script to convert GitHub Markdown variant into something approximating that used by Pandoc.

Currently it handles the following conversions:
 
- GitHub LaTeX math (bracket delimited) → Pandoc LaTeX math (dollar sign delimited)
- GitHub delimited code blocks (triple backticks) → Pandoc delimited code blocks (tildes)

I'm sure the same could be done more compactly with some Sed magic, but then I prefer Python the use of Python's `re` module for it's readability.

# Installation

On a Unix-like system: Put it somewhere in your path and make it executable.

On Windows: run it as a Python script.

# Usage

The script takes input from either a file (via `-i` argument) or stdin (default) and writes to stdout.

Example stand-alone usage:

    github2pandoc.py -i example.md > example.pdoc

Example usage with Pandoc (LaTeX as final output):

    github2pandoc.py -i example.md | pandoc -s -f markdown -t latex -o example.tex
    

# Status

This was thrown together quickly, so I haven't done any extensive testing except to run a few of my own documents through it. Additions, bug fixes, suggestions welcome.