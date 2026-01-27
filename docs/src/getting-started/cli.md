# Command-line interface

Nomage can be used directly from the command line through its dedicated command-line
interface (CLI), which provides a fast and convenient alternative to the
[Python API :material-language-python:](./api.md) for common use cases.

## Interface

The CLI is intentionally minimal and focused on built-in naming conventions.
Its full usage and available options can be discovered using help flag:

```txt
$ nomage --help
--8<-- "getting-started/cli_help.txt"
```

## Exit codes

The CLI uses standard exit codes:

- `0` - success
- `1` - runtime failure: unrecognized naming convention
- `2` - invalid arguments or failed check

These exit codes can be used in scripts and CI pipelines.

## Limitations

- Only [built-in naming conventions](../learn/conventions.md) are supported.
- No custom rules or plugins can be loaded.
- For advanced workflows, use the [Python API :material-language-python:](./api.md).
