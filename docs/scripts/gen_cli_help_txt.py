#!/usr/bin/env python3
"""Generate the CLI help text page."""

from pathlib import Path

from nomage._cli import create_parser

parser = create_parser()
parser.prog = "nomage"

output_path = Path("src/learn/cli_help.txt")
with output_path.open("w") as f:
    parser.print_help(file=f)
