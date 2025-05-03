"""Command-line interface."""

import argparse
import sys
from importlib.metadata import metadata


def main(_args: list[str] | None = None, /) -> None:
    if _args is None:
        _args = sys.argv[1:]

    parser = create_parser()
    args = parser.parse_args(_args)

    if args.version:
        pkg_metadata = metadata(__package__)
        print(pkg_metadata["Version"])

    sys.exit(0)


def create_parser() -> argparse.ArgumentParser:
    pkg_metadata = metadata(__package__)
    parser = argparse.ArgumentParser(
        description=f"{pkg_metadata['Name']} - {pkg_metadata['Summary']}",
    )
    parser.add_argument(
        "-V", "--version", action="store_true", help="print version and exit"
    )
    return parser
