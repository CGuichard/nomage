"""Tests for the Nomage API functionalities."""

import re

import pytest

from nomage import Identifier, NamingConvention, builtins_conventions, naming
from nomage.exceptions import (
    UnknownNamingConventionError,
    UnrecognizedNamingConventionError,
)


def test_naming_convention_match() -> None:
    """NamingConvention.match correctly identifies valid identifiers."""
    nc = NamingConvention(
        names=("flatcase", "lowercase"),
        match_regex=re.compile(r"^[a-z][a-z0-9]*$"),
        parser=lambda id_str: (id_str.lower(),),
        converter=lambda components: "".join(components),
    )

    identifier1 = "myidentifier"
    identifier2 = "MyIdentifier"
    assert nc.match_regex.match(identifier1) is not None
    assert nc.match(identifier1)
    assert nc.match_regex.match(identifier2) is None
    assert not nc.match(identifier2)


def test_naming_convention_parser() -> None:
    """NamingConvention.parser correctly splits identifier into components."""
    nc = NamingConvention(
        names=("snake_case", "snail_case", "pothole_case"),
        match_regex=re.compile(r"^[a-z][a-z0-9]*(_[a-z0-9]*)*$"),
        parser=lambda id_str: tuple(id_str.lower().split("_")),
        converter=lambda components: "_".join(components),
    )
    assert nc.parser("my_identifier") == ("my", "identifier")


def test_naming_convention_converter() -> None:
    """NamingConvention.converter correctly formats components to convention."""
    nc = NamingConvention(
        names=("snake_case", "snail_case", "pothole_case"),
        match_regex=re.compile(r"^[a-z][a-z0-9]*(_[a-z0-9]*)*$"),
        parser=lambda id_str: tuple(id_str.lower().split("_")),
        converter=lambda components: "_".join(components),
    )
    assert nc.converter(("my", "identifier")) == "my_identifier"


def test_naming_convention_eq() -> None:
    """NamingConvention.__eq__ works with convention names."""
    nc = NamingConvention(
        names=("flatcase", "lowercase"),
        match_regex=re.compile(r"^[a-z][a-z0-9]*$"),
        parser=lambda id_str: (id_str.lower(),),
        converter=lambda components: "".join(components),
    )
    assert nc == "flat"
    assert nc == "lower"
    assert nc != "snake"
    assert nc != "pascal"
    assert nc != 1, (
        "NamingConvention can only be tested equal "
        "against NamingConvention or str objects"
    )


def test_identifier_str() -> None:
    """Identifier.__str__ returns the correctly formatted identifier."""
    snake_nc = NamingConvention(
        names=("snake_case",),
        match_regex=re.compile(r"^[a-z][a-z0-9]*(_[a-z0-9]*)*$"),
        parser=lambda id_str: tuple(id_str.lower().split("_")),
        converter=lambda components: "_".join(components),
    )
    id_naming = Identifier(components=("my", "identifier"), convention=snake_nc)
    assert str(id_naming) == "my_identifier"


def test_identifier_to() -> None:
    """Identifier.to correctly converts to another naming convention."""
    snake_nc = NamingConvention(
        names=("snake_case",),
        match_regex=re.compile(r"^[a-z][a-z0-9]*(_[a-z0-9]*)*$"),
        parser=lambda id_str: tuple(id_str.lower().split("_")),
        converter=lambda components: "_".join(components),
    )
    kebab_nc = NamingConvention(
        names=("kebab-case",),
        match_regex=re.compile(r"^[a-z][a-z0-9]*(-[a-z][a-z0-9]*)*$"),
        parser=lambda id_str: tuple(id_str.lower().split("-")),
        converter=lambda components: "-".join(components),
    )
    id_naming = Identifier(components=("my", "identifier"), convention=snake_nc)

    assert id_naming.to(kebab_nc) == "my-identifier"


def test_identifier_to_str() -> None:
    """Identifier.to accepts string names of built-in conventions."""
    snake_nc = NamingConvention(
        names=("snake_case",),
        match_regex=re.compile(r"^[a-z][a-z0-9]*(_[a-z0-9]*)*$"),
        parser=lambda id_str: tuple(id_str.lower().split("_")),
        converter=lambda components: "_".join(components),
    )
    kebab_nc = NamingConvention(
        names=("kebab-case",),
        match_regex=re.compile(r"^[a-z][a-z0-9]*(-[a-z][a-z0-9]*)*$"),
        parser=lambda id_str: tuple(id_str.lower().split("-")),
        converter=lambda components: "-".join(components),
    )
    id_naming = Identifier(components=("my", "identifier"), convention=snake_nc)

    assert id_naming.to(kebab_nc) == id_naming.to("kebab-case")


def test_identifier_to_str_unknown() -> None:
    """Identifier.to returns original format for unknown conventions."""
    snake_nc = NamingConvention(
        names=("snake_case",),
        match_regex=re.compile(r"^[a-z][a-z0-9]*(_[a-z0-9]*)*$"),
        parser=lambda id_str: tuple(id_str.lower().split("_")),
        converter=lambda components: "_".join(components),
    )
    id_naming = Identifier(components=("my", "identifier"), convention=snake_nc)

    with pytest.raises(UnknownNamingConventionError):
        id_naming.to("unknown")


def test_naming() -> None:
    """Function `naming` correctly identifies and parses identifiers."""
    conventions = builtins_conventions()
    components = ("my", "identifier")
    n1 = naming("my_identifier")
    n2 = naming("myIdentifier")
    n3 = naming("MyIdentifier")

    assert n1.components == components
    assert n1.convention == conventions.get("snake")
    assert n2.components == components
    assert n2.convention == conventions.get("camel")
    assert n3.components == components
    assert n3.convention == conventions.get("pascal")


def test_naming_unknown() -> None:
    """Function `naming` returns None for unrecognized identifiers."""
    with pytest.raises(UnrecognizedNamingConventionError):
        naming("my__identifier")
