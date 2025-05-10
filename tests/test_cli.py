"""Tests for the Nomage command-line interface."""

from importlib.metadata import metadata

import pytest

from nomage._cli import main


def test_no_args() -> None:
    """Running the CLI without arguments shows help and exits with error."""
    with pytest.raises(SystemExit) as exc_info:
        main([])
    assert exc_info.value.code == 2


def test_help(capsys: pytest.CaptureFixture[str]) -> None:
    """Flag --help displays usage information and exits successfully."""
    with pytest.raises(SystemExit) as exc_info:
        main(["--help"])

    capture = capsys.readouterr()
    assert exc_info.value.code == 0
    assert "usage:" in capture.out


def test_version_flag(capsys: pytest.CaptureFixture[str]) -> None:
    """Flag --version displays the correct package version."""
    m = metadata("nomage")
    with pytest.raises(SystemExit) as exc_info:
        main(["--version"])

    capture = capsys.readouterr()
    assert exc_info.value.code == 0
    assert m["version"] in capture.out


def test_detection(capsys: pytest.CaptureFixture[str]) -> None:
    """Passing a valid identifier correctly detects its naming convention."""
    with pytest.raises(SystemExit) as exc_info:
        main(["myIdentifier"])

    capture = capsys.readouterr()
    assert exc_info.value.code == 0
    assert "camelCase" in capture.out


def test_detection_error(capsys: pytest.CaptureFixture[str]) -> None:
    """Passing an invalid identifier returns an appropriate error message."""
    with pytest.raises(SystemExit) as exc_info:
        main(["my-Identifier"])

    capture = capsys.readouterr()
    assert exc_info.value.code == 1
    stderr = capture.err.lower()
    assert "no matching" in stderr
    assert "no matching" in stderr


def test_check() -> None:
    """Option --check successfully verifies a matching naming convention."""
    with pytest.raises(SystemExit) as exc_info:
        main(["myIdentifier", "--check", "camel"])

    assert exc_info.value.code == 0


def test_check_wrong(capsys: pytest.CaptureFixture[str]) -> None:
    """Option --check fails with error when convention doesn't match."""
    with pytest.raises(SystemExit) as exc_info:
        main(["myIdentifier", "--check", "snake"])

    capture = capsys.readouterr()
    assert exc_info.value.code == 2
    stderr = capture.err.lower()
    assert "not matching" in stderr
    assert "snake" in stderr


def test_check_unrecognized(capsys: pytest.CaptureFixture[str]) -> None:
    """Option --check fails with error when convention is unknown."""
    with pytest.raises(SystemExit) as exc_info:
        main(["myIdentifier", "--check", "unknown"])

    capture = capsys.readouterr()
    assert exc_info.value.code == 1
    stderr = capture.err.lower()
    assert "could not find" in stderr
    assert "unknown" in stderr


def test_convert(capsys: pytest.CaptureFixture[str]) -> None:
    """Option --to successfully converts identifier to target convention."""
    with pytest.raises(SystemExit) as exc_info:
        main(["myIdentifier", "--to", "snake"])

    capture = capsys.readouterr()
    assert exc_info.value.code == 0
    assert "my_identifier" in capture.out


def test_convert_error(capsys: pytest.CaptureFixture[str]) -> None:
    """Option --to fails with error when target convention is unknown."""
    with pytest.raises(SystemExit) as exc_info:
        main(["myIdentifier", "--to", "unknown"])

    capture = capsys.readouterr()
    assert exc_info.value.code == 1
    stderr = capture.err.lower()
    assert "could not find" in stderr
    assert "unknown" in stderr
