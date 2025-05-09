"""CLI test."""

from importlib.metadata import metadata

import pytest

from nomage._cli import main


def test_no_args() -> None:
    """Running CLI with no arguments nor options."""
    with pytest.raises(SystemExit) as exc_info:
        main([])
    assert exc_info.value.code == -1


def test_help(capsys: pytest.CaptureFixture[str]) -> None:
    """Running CLI with --help."""
    with pytest.raises(SystemExit) as exc_info:
        main(["--help"])

    capture = capsys.readouterr()
    assert exc_info.value.code == 0
    assert "usage:" in capture.out


def test_version_flag(capsys: pytest.CaptureFixture[str]) -> None:
    """Running CLI with "--version" to print package version number."""
    m = metadata("nomage")
    with pytest.raises(SystemExit) as exc_info:
        main(["--version"])

    capture = capsys.readouterr()
    assert exc_info.value.code == 0
    assert m["version"] in capture.out
