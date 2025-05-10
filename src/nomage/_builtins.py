"""
Nomage - built-in naming conventions.

This module provides a collection of common naming conventions used in programming,
such as camelCase, snake_case, kebab-case, etc. The conventions are provided by the
function `builtins_conventions` as a mapping for looking up conventions by their names.
"""

import re
from collections.abc import Iterator, Mapping, Sequence

from nomage.convention import NamingConvention


class _NamingConventionMap(Mapping[str, NamingConvention]):
    def __init__(self, conventions: Sequence[NamingConvention], /) -> None:
        self._size = len(conventions)
        self._map, self._index = self._compute(conventions)

    def __getitem__(self, key: str) -> NamingConvention:
        return self._index[NamingConvention.get_name_index(key)]

    def __len__(self) -> int:
        return self._size

    def __iter__(self) -> Iterator[str]:
        return iter(self._map)

    def _compute(
        self, items: Sequence[NamingConvention]
    ) -> tuple[Mapping[str, NamingConvention], Mapping[str, NamingConvention]]:
        items_map: dict[str, NamingConvention] = {}
        items_index: dict[str, NamingConvention] = {}
        for nc in items:
            for name in nc.names:
                items_map[name] = nc
                items_index[NamingConvention.get_name_index(name)] = nc
        return items_map, items_index


_BUILTINS_CONVENTIONS: Mapping[str, NamingConvention] = _NamingConventionMap(
    (
        NamingConvention(
            names=("flatcase", "lowercase"),
            match_regex=re.compile(r"^[a-z][a-z0-9]*$"),
            parser=lambda id_str: (id_str.lower(),),
            converter=lambda components: "".join(components),
        ),
        NamingConvention(
            names=("UPPERCASE", "SCREAMINGCASE"),
            match_regex=re.compile(r"^[A-Z][A-Z0-9]*$"),
            parser=lambda id_str: (id_str.lower(),),
            converter=lambda components: "".join(components).upper(),
        ),
        NamingConvention(
            names=("camelCase", "dromedaryCase"),
            match_regex=re.compile(r"^[a-z][a-zA-Z0-9]*$"),
            parser=lambda id_str: tuple(
                re.sub(r"([A-Z])", r" \1", id_str).lower().split()
            ),
            converter=lambda components: "".join(
                [components[0], *(w.capitalize() for w in components[1:])]
            ),
        ),
        NamingConvention(
            names=("PascalCase", "UpperCamelCase", "StudlyCase"),
            match_regex=re.compile(r"^[A-Z][a-zA-Z0-9]*$"),
            parser=lambda id_str: tuple(
                re.sub(r"([A-Z])", r" \1", id_str).lower().split()
            ),
            converter=lambda components: "".join(w.capitalize() for w in components),
        ),
        NamingConvention(
            names=("snake_case", "snail_case", "pothole_case"),
            match_regex=re.compile(r"^[a-z][a-z0-9]*(_[a-z][a-z0-9]*)*$"),
            parser=lambda id_str: tuple(id_str.lower().split("_")),
            converter=lambda components: "_".join(components),
        ),
        NamingConvention(
            names=(
                "ALL_CAPS",
                "SCREAMING_SNAKE_CASE",
                "MACRO_CASE",
                "CONSTANT_CASE",
                "ENV_VAR_CASE",
            ),
            match_regex=re.compile(r"^[A-Z][A-Z0-9]*(_[A-Z][A-Z0-9]*)*$"),
            parser=lambda id_str: tuple(id_str.lower().split("_")),
            converter=lambda components: "_".join(w.upper() for w in components),
        ),
        NamingConvention(
            names=("camel_Snake_Case",),
            match_regex=re.compile(r"^[a-z]+[a-z0-9]*(_[A-Z]+[a-z0-9]*)*$"),
            parser=lambda id_str: tuple(id_str.lower().split("_")),
            converter=lambda components: "_".join(
                [components[0], *(w.capitalize() for w in components[1:])]
            ),
        ),
        NamingConvention(
            names=("kebab-case", "dash-case", "lisp-case", "spinal-case"),
            match_regex=re.compile(r"^[a-z][a-z0-9]*(-[a-z][a-z0-9]*)*$"),
            parser=lambda id_str: tuple(id_str.lower().split("-")),
            converter=lambda components: "-".join(components),
        ),
        NamingConvention(
            names=("COBOL-CASE", "SCREAMING-TRAIN-CASE", "SCREAMING-KEBAB-CASE"),
            match_regex=re.compile(r"^[A-Z][A-Z0-9]*(-[A-Z][A-Z0-9]*)*$"),
            parser=lambda id_str: tuple(id_str.lower().split("-")),
            converter=lambda components: "-".join(w.upper() for w in components),
        ),
        NamingConvention(
            names=("Train-Case", "Http-Header-Case"),
            match_regex=re.compile(r"^[A-Z]+[a-z0-9]*(-[A-Z]+[a-z0-9]*)*$"),
            parser=lambda id_str: tuple(id_str.lower().split("-")),
            converter=lambda components: "-".join(w.capitalize() for w in components),
        ),
    )
)


def builtins_conventions() -> Mapping[str, NamingConvention]:
    """
    Provide collection of common naming convention as a mapping for lookup by name.

    This function provides a collection of common naming conventions used in
    programming, such as camelCase, snake_case, kebab-case, etc.
    The conventions are provided as a mapping for looking up conventions
    by their names.

    Examples:
        >>> conventions = builtins_conventions()

        Usage of the `get` method is recommended for None fallback.

        >>> conventions.get("PascalCase")
        NamingConvention(...)
        >>> conventions.get("no-name")  # None

        Keys are not case-sensitive, and ignore "case" word,
        hyphens, underscores.

        >>> conventions.get("PascalCase") == conventions.get("pascal")
        True
        >>> conventions.get("snake") == conventions.get("Snake-Case")
        True

    Returns:
        A mapping with str keys and NamingConvention values.
    """
    return _BUILTINS_CONVENTIONS
