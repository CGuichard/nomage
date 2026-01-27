# Python API

Nomage provides a Python API for working programmatically with naming conventions.
It is designed to allow you to detect, parse, convert, and define naming conventions,
making it easier to work with different conventions from multiple sources.

## When to use the Python API

The Python API is recommended when you need:

- Custom/user-defined naming conventions.
- Programmatic access to detection and conversion results.
- Integration into existing Python tools or pipelines.
- More control over error handling and behavior.

!!! tip
    If you only need to apply the built-in conventions from the command line, the [CLI :material-console:](./cli.md) may be sufficient.

## Core capabilities

The Python API exposes the full feature set of Nomage:

- **Convention detection**:
  Automatically identify the naming convention used by an identifier.

- **Identifier parsing**:
  Split identifiers into their logical components, independent of case style or separators.

- **Convention conversion**:
  Convert identifiers between supported naming conventions.

- **Built-in conventions**:
  Access a curated set of common conventions such as `camelCase`, `snake_case`, and `kebab-case`.

- **Custom conventions**:
  Define and register your own conventions for project-specific rules.

## Next steps

- See usage examples for [detection](../learn/usage/detect.md), [check](../learn/usage/check.md),
  and [conversion](../learn/usage/convert.md) of an identifier's naming convention.
- Explore the detailed [:material-language-python: API reference](../reference/api/nomage/__init__.md)
  for available functions and classes.
- Learn how to declare custom naming conventions.
