"""
Nomage - naming convention API.

This module provides a structured representation of a naming convention using
regular expressions, parsing, and converting logic. It allows for validation,
parsing, and transformation of identifiers according to specific naming patterns.
"""

import re
from collections.abc import Callable
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class NamingConvention:
    """
    Represents a naming convention used to validate, parse, and convert identifiers.

    A naming convention defines how identifiers should be structured and provides
    methods to validate, parse, and convert identifiers according to the convention.

    Attributes:
        names: A tuple of names/aliases for this naming convention.
        match_regex: A compiled regular expression used to match identifiers
            that follow this convention.
        parser: A function that takes an identifier and returns a tuple of its
            components in lower case.
        converter: A function that takes a tuple of components and returns an
            identifier formatted according to this convention.
    """

    names: tuple[str, ...]
    match_regex: re.Pattern[str]
    parser: Callable[[str], tuple[str, ...]]
    converter: Callable[[tuple[str, ...]], str]

    @staticmethod
    def get_name_index(name: str) -> str:
        """Compute convention name index."""
        return (
            name.lower()
            .removesuffix("case")
            .replace(" ", "")
            .replace("_", "")
            .replace("-", "")
        )

    def match(self, id_str: str, /) -> bool:
        """
        Check if the given identifier matches this naming convention.

        Args:
            id_str: The identifier string to check against the convention.

        Returns:
            True if the identifier matches the convention's regular expression,
            False otherwise.
        """
        return self.match_regex.match(id_str) is not None

    def __hash__(self) -> int:
        return hash(self.match_regex)  # pragma: no cover

    def __eq__(self, value: object, /) -> bool:
        if isinstance(value, NamingConvention):
            return self.match_regex == value.match_regex
        if isinstance(value, str):
            return any(
                self.get_name_index(value) == self.get_name_index(n) for n in self.names
            )
        return False
