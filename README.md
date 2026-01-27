# Nomage

<div align="center" style="margin:40px;">

<img src="https://raw.githubusercontent.com/CGuichard/nomage/main/docs/src/assets/img/logo.png" alt="Nomage logo" style="margin-bottom: 20px" width="500"/>

_Utility for parsing and converting naming conventions_

<!-- --8<-- [start:badges] -->

[![Language](https://img.shields.io/badge/language-python≥3.10-3776ab?style=flat-square)](https://www.python.org/)
![License](https://img.shields.io/badge/license-MIT-yellow?style=flat-square)
[![Documentation](https://img.shields.io/badge/documentation-Material%20for%20MkDdocs-0a507a?style=flat-square)](https://CGuichard.github.io/nomage/)
![Style](https://img.shields.io/badge/style-ruff-9a9a9a?style=flat-square)
![Lint](https://img.shields.io/badge/lint-ruff,%20mypy-brightgreen?style=flat-square)
![Security](https://img.shields.io/badge/security-bandit,%20pip--audit-purple?style=flat-square)
[![PyPI - Version](https://img.shields.io/pypi/v/nomage?style=flat-square)](https://pypi.org/project/nomage/)
[![Tests](https://img.shields.io/github/actions/workflow/status/CGuichard/nomage/check.yml?branch=main&label=Test)](https://github.com/CGuichard/nomage/actions/workflows/check.yml)
[![Coverage](https://raw.githubusercontent.com/CGuichard/nomage/refs/heads/gh-tests-coverages/data/main/badge.svg)](https://github.com/CGuichard/nomage/actions/workflows/check.yml)

[Pull Request](https://github.com/CGuichard/nomage/pulls) **·**
[Bug Report](https://github.com/CGuichard/nomage/issues/new?template=bug_report.md) **·**
[Feature Request](https://github.com/CGuichard/nomage/issues/new?template=feature_request.md)

<!-- --8<-- [end:badges] -->

</div>

<!-- --8<-- [start:introduction] -->

Nomage is a Python tool that helps you work with different [naming conventions](https://en.wikipedia.org/wiki/Naming_convention_(programming)) in your code. It provides tools to detect, parse, and convert identifiers between various conventions like camelCase, snake_case, kebab-case, and more.

Features:

- 🔍 **Automatic Detection**: Identify the naming convention of any identifier
- 🔄 **Easy Conversion**: Transform identifiers between different conventions
- 🛠️ **Flexible API**: Use it programmatically or via command-line
- 📦 **Built-in Conventions**: Support for common naming patterns
- 🔌 **Extensible**: Create and use your own custom conventions
- 🔎 **Smart Lookup**: Case-insensitive and separator-insensitive convention lookup

<!-- --8<-- [end:introduction] -->

## Table of Contents

- [Getting started](#getting-started)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Detecting Conventions](#detecting-conventions)
    - [Checking Conventions](#checking-conventions)
    - [Converting Identifiers](#converting-identifiers)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Getting started

### Installation

Install `nomage` with pip:

```bash
pip install nomage
```

Install from source:

```bash
pip install git+https://github.com/CGuichard/nomage.git
# or with a specific version
pip install git+https://github.com/CGuichard/nomage.git@<tag>
```

### Usage

#### Detecting Conventions

```python
from nomage import naming

# Detect convention
id_naming = naming("my_identifier")
print(id_naming.convention.names)
# ('snake_case', 'snail_case', 'pothole_case')

# Handle unknown conventions
try:
    naming("my-_-identifier")
except ValueError:
    print("Unrecognized convention")
```

```bash
$ nomage my_identifier
Detected: snake_case / snail_case / pothole_case

$ nomage my-_-identifier
No matching naming convention, invalid identifier 'my-_-identifier'
```

#### Checking Conventions

```python
from nomage import naming

id_naming = naming("my_identifier")
print(id_naming.convention == "snake")  # True
print(id_naming.convention == "pascal")  # False
```

```bash
$ nomage my_identifier --check snake

$ nomage my_identifier --check pascal
Not matching convention: PascalCase / UpperCamelCase / StudlyCase
```

#### Converting Identifiers

```python
from nomage import naming

id_naming = naming("my-identifier")

# Convert to different conventions
print(id_naming.to("snake_case")) # my_identifier
print(id_naming.to("camelCase")) # myIdentifier
```

```bash
$ nomage my-identifier --to snake
my_identifier

$ nomage my_identifier --to camelCase
myIdentifier

$ nomage my_identifier --to test
Could not find naming convention 'test'
```

## Contributing

If you want to contribute to this project please check [CONTRIBUTING.md](CONTRIBUTING.md).

Everyone contributing to this project is expected to treat other people with respect,
and more generally to follow the guidelines articulated by our [Code of Conduct](./CODE_OF_CONDUCT.md).

## License

Copyright &copy; 2026, Clément GUICHARD

Nomage is licensed under the MIT license. A copy of this license is provided in the [LICENSE](./LICENSE) file.

## Acknowledgements

This package was created with [Cookiecutter](https://github.com/cookiecutter/cookiecutter)
from the project template [CGuichard/cookiecutter-pypackage](https://github.com/CGuichard/cookiecutter-pypackage).
