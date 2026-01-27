# Detection

The most basic use-case of Nomage is to detect the naming convention used
for an identifier.

The main entrypoint is a function called [`naming()`](../../reference/api/nomage/naming.md#nomage.naming.naming),
that takes for argument an identifier and return an object
[`Identifier`](../../reference/api/nomage/naming.md#nomage.naming.Identifier) or `None`.

## Python

You can detect which naming convention is used with:

```python
>>> from nomage import naming
>>> id_naming = naming("my-identifier")
>>> id_naming.convention.names
('kebab-case', 'dash-case', 'lisp-case', 'spinal-case')
```

If no convention is detected, `ValueError` is raised.

```python
>>> from nomage import naming
>>> naming("my-_-identifier")
nomage.exceptions.UnrecognizedNamingConventionError: no matching naming convention, invalid identifier 'my-_-identifier'
```

## CLI

Check it from a terminal:

=== "Terminal"

    <!-- termynal -->

    ```bash
    $ nomage my-identifier
    Detected: kebab-case / dash-case / lisp-case / spinal-case
    ```

=== "Command"

    ```console
    nomage my-identifier
    ```

Unrecognized identifier will fail with a return code not equal to `0`.

=== "Terminal"

    <!-- termynal -->

    ```bash
    $ nomage my-\_-identifier
    No matching naming convention, invalid identifier 'my-_-identifier'
    ```

=== "Command"

    ```console
    nomage my-_-identifier
    ```
