"""
Nomage - identifier and naming API.

This module provides the core functionality for working with naming conventions,
including parsing identifiers and transforming them between different conventions.
"""

from collections.abc import Iterable
from dataclasses import dataclass

from nomage._builtins import builtins_conventions
from nomage.convention import NamingConvention
from nomage.exceptions import (
    UnknownNamingConventionError,
    UnrecognizedNamingConventionError,
)

_BUILTINS_CONVENTIONS = builtins_conventions()
BUILTINS_CONVENTIONS = tuple(_BUILTINS_CONVENTIONS.values())


@dataclass(frozen=True, slots=True)
class Identifier:
    """
    Represents a parsed identifier with its components and associated convention.

    This class holds the components of an identifier and its original naming
    convention, allowing for transformation to other conventions.

    Attributes:
        components: The parsed components of the identifier in lower case.
        convention: The naming convention that was used to parse the identifier.
    """

    components: tuple[str, ...]
    convention: NamingConvention

    def to(self, nc: str | NamingConvention, /) -> str:
        """
        Transform the identifier to another naming convention.

        Args:
            nc: Either a string name of a convention or a NamingConvention obj.

        Raises:
            UnknownNamingConventionError:
                Raised when `nc` is an str and no matching naming convention found.

        Returns:
            The identifier transformed to the target convention. If the target
            convention is not found (when using a string name), returns the
            string representation of the current identifier.
        """
        if isinstance(nc, str):
            _nc = _BUILTINS_CONVENTIONS.get(nc)
            if _nc is None:
                raise UnknownNamingConventionError(nc)
            nc = _nc
        return nc.converter(self.components)

    def __str__(self) -> str:
        return self.convention.converter(self.components)


def naming(
    id_str: str, /, conventions: Iterable[NamingConvention] = BUILTINS_CONVENTIONS
) -> Identifier:
    """
    Parse an str identifier and return an Identifier obj if it matches a convention.

    Args:
        id_str: The identifier string to parse.
        conventions: An iterable of naming conventions to try matching against.
            Defaults to the built-in conventions.

    Raises:
        UnrecognizedNamingConventionError:
            Raised when no matching convention for `id_str`.

    Returns:
        An Identifier obj if the identifier matches any of the conventions.
    """
    for nc in conventions:
        if nc.match(id_str):
            return Identifier(convention=nc, components=nc.parser(id_str))

    raise UnrecognizedNamingConventionError(id_str)
