"""Basic package test."""


def test_package_import() -> None:
    """Import package."""
    import nomage  # noqa: F401, PLC0415


def test_package_version_is_defined() -> None:
    """Check imported package have __version__ defined."""
    import nomage  # noqa: PLC0415

    assert nomage.__version__ != "undefined"
