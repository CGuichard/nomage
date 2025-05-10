"""Command-line interface for Nomage.

This module provides a CLI for inspecting and converting identifier naming conventions.
It allows users to check the convention of an identifier, convert it to another
convention, or print the package version.

Examples:
    $ nomage MyIdentifier
    Detected: PascalCase / UpperCamelCase / StudlyCase
    $ nomage MyIdentifie_R
    Unrecognized naming convention for: MyIdentifie_R
    $ nomage MyIdentifier --check pascal
    Matching.
    $ nomage MyIdentifier --check httpheader
    Not matching convention: Train-Case / Http-Header-Case
    $ nomage MyIdentifier --to snake
    my_identifier
    $ nomage MyIdentifier --to snack
    Unrecognized naming convention: snack
"""

import argparse
import sys
from collections.abc import Mapping
from importlib.metadata import metadata

from nomage._builtins import builtins_conventions
from nomage.convention import NamingConvention
from nomage.exceptions import (
    UnknownNamingConventionError,
    UnrecognizedNamingConventionError,
)
from nomage.naming import naming


def main(_args: list[str] | None = None, /) -> None:
    """
    Entry point for the Nomage command-line interface.

    Parses command-line arguments and performs actions such as printing the
    version, checking an identifier's convention, or converting an identifier
    to another convention.

    Args:
        _args: Optional list of arguments to parse. If None, uses sys.argv[1:].
    """
    if _args is None:  # pragma: no cover
        _args = sys.argv[1:]

    parser = create_parser()
    args = parser.parse_args(_args)

    if args.version:
        pkg_metadata = metadata(__package__)
        print(pkg_metadata["Version"])
        sys.exit(0)

    if not args.identifier:
        parser.print_help()
        sys.exit(2)

    try:
        id_naming = naming(args.identifier)

        if not args.check_convention and not args.to_convention:
            print("Detected:", " / ".join(id_naming.convention.names))

        conventions = builtins_conventions()

        if args.check_convention:
            nc = _get_naming_convention(args.check_convention, conventions)
            if not nc.match(str(id_naming)):
                print(
                    "Not matching convention:",
                    " / ".join(nc.names),
                    file=sys.stderr,
                )
                sys.exit(2)

        if args.to_convention:
            nc = _get_naming_convention(args.to_convention, conventions)
            print(id_naming.to(nc))

    except (UnknownNamingConventionError, UnrecognizedNamingConventionError) as err:
        print(str(err).capitalize(), file=sys.stderr)
        sys.exit(1)
    else:
        sys.exit(0)


def _get_naming_convention(
    name: str, conventions: Mapping[str, NamingConvention]
) -> NamingConvention:
    nc = conventions.get(name)
    if nc is None:
        raise UnknownNamingConventionError(name)
    return nc


def create_parser() -> argparse.ArgumentParser:
    """
    Create and configure the argument parser for the CLI.

    Returns:
        An ArgumentParser instance configured for the Nomage CLI.
    """
    pkg_metadata = metadata(__package__)
    parser = argparse.ArgumentParser(
        description=f"{pkg_metadata['Name']} - {pkg_metadata['Summary']}",
    )
    parser.add_argument(
        "-V", "--version", action="store_true", help="print version and exit"
    )
    parser.add_argument("-t", "--to", dest="to_convention")
    parser.add_argument("-c", "--check", dest="check_convention")
    parser.add_argument("identifier", nargs="?")
    return parser
