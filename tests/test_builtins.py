"""Tests for the Nomage built-in naming conventions."""

from collections.abc import Container, Iterable, Mapping, Sized

from nomage import builtins_conventions


def test_builtins_conventions_is_mapping() -> None:
    """Function `builtins_conventions` returns a valid Mapping instance."""
    conventions = builtins_conventions()
    assert isinstance(conventions, Mapping)
    assert isinstance(conventions, Container)
    assert isinstance(conventions, Iterable)
    assert isinstance(conventions, Sized)
    assert len(conventions)


def test_builtins_conventions_values() -> None:
    """Function `builtins_conventions` contains all expected naming conventions."""
    conventions = builtins_conventions()
    assert conventions.get("LOWERCASE") is not None
    assert conventions.get("UPPERCASE") is not None
    assert conventions.get("snake_case") is not None
    assert conventions.get("kebab-case") is not None
    assert conventions.get("camelCase") is not None
    assert conventions.get("PascalCase") is not None


def test_builtins_conventions_key_lookup() -> None:
    """Function `builtins_conventions` key lookup is case and separator insensitive."""
    conventions = builtins_conventions()
    assert conventions.get("snake_case") == conventions.get("SNAKE_CASE")
    assert conventions.get("snake_case") == conventions.get("snake")
    assert conventions.get("snake_case") == conventions.get("snake-case")
    assert conventions.get("snake_case") == conventions.get("snakecase")
