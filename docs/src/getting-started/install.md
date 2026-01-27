# Installation

:material-arrow-right-circle: Python ≥ 3.10 is required.

Nomage is available as `nomage` on PyPI.

## Install in Python environment

The following section will tell you about the installation of the package
in your Python environment, allowing usage of both the [CLI :material-console:](./cli.md)
and the [Python API :material-language-python:](./api.md).

!!! tip
    The use of a virtual environment is greatly recommended :material-shield-check:.

### Pip from PyPI

You can install `nomage` easily with `pip`:

<!-- termynal -->

```bash
$ pip install nomage
---> 100%
Installed!
```

### Pip from source

You can install from the code source with the repository:

<!-- termynal -->

```bash
$ pip install git+https://github.com/CGuichard/nomage.git@main
---> 100%
Installed from source!
```

## Install for terminal

In this section you will learn how to install **only** the [CLI :material-console:](./cli.md).

### Pipx

Pipx is a tool that let you install and run Python "applications" in isolated
environments, and exposes the commands in your user environment.

You can install `nomage` with `pipx`:

<!-- termynal -->

```bash
$ pipx install nomage
---> 100%
Installed!
```

!!! info
    Learn more about [Pipx :octicons-link-external-24:](https://pipx.pypa.io/){ target="_blank" }.

### UV

UV is an extremely fast Python package and project manager. One of its features is "Tools",
that exposes commands from Python packages just like Pipx.

You can install `nomage` with `uv tool`:

<!-- termynal -->

```bash
$ uv tool install nomage
---> 100%
Installed!
```

!!! info
    Learn more about [uv :octicons-link-external-24:](https://docs.astral.sh/uv/){ target="_blank" }
    and [uv tool :octicons-link-external-24:](https://docs.astral.sh/uv/concepts/tools/){ target="_blank" }.
