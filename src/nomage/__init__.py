"""Nomage - Utility for parsing and converting naming conventions.

Nomage provides a simple API to work with different naming conventions in Python.
It can detect, parse, and convert identifiers between various conventions like
camelCase, snake_case, kebab-case, etc.

The package includes:

- A command-line interface for quick conversions
- A Python API for programmatic usage
- Built-in support for common naming conventions
- Case-insensitive convention lookup
- Custom convention support

Examples:
    Automatic detection
    >>> from nomage import naming
    >>> id_ = naming("myIdentifier")

    Convert to other conventions
    >>> id_.to("snake_case")
    'my_identifier'
    >>> id_.to("kebab-case")
    'my-identifier'
"""

from importlib.metadata import PackageNotFoundError, version

from ._builtins import builtins_conventions
from .convention import NamingConvention
from .naming import Identifier, naming

__all__ = ["Identifier", "NamingConvention", "builtins_conventions", "naming"]

try:
    __version__ = version(__name__)
except PackageNotFoundError:  # pragma: no cover
    # package is not installed
    __version__ = "undefined"
