# Convert

The most useful feature of Nomage is converting an identifier to another
naming convention.

## Python

You can convert to another naming convention with:

```python
>>> from nomage import naming
>>> id_naming = naming("my-identifier")
>>> id_naming.to("pascal")
"MyIdentifier"
```

Unknown naming conventions will simply return source convention

```python
>>> from nomage import naming
>>> id_naming = naming("my-identifier")
>>> id_naming.to("unknown")
nomage.exceptions.UnknownNamingConventionError: could not find naming convention 'unknown'
```

## CLI

Convert from a terminal:

=== "Terminal"

    <!-- termynal -->

    ```bash
    $ nomage my-identifier --to pascal
    MyIdentifier
    ```

=== "Command"

    ```console
    nomage my-identifier --to pascal
    ```

Unknown naming convention will fail with a return code not equal to `0`.

=== "Terminal"

    <!-- termynal -->

    ```bash
    $ nomage my-identifier --to test
    Could not find naming convention 'test'
    ```

=== "Command"

    ```console
    nomage my-identifier --to test
    ```
