# Check / Assert

More than [detecting](./detect.md) the naming convention of an identifier you can check it's the one you expect.

## Python

You can detect which naming convention is used with:

```python
>>> from nomage import naming
>>> id_naming = naming("my-identifier")
>>> id_naming.convention == "kebab"
True
```

Of course wrong returns `False`.

```python
>>> from nomage import naming
>>> id_naming = naming("my-identifier")
>>> id_naming.convention == "snake"
False
```

## CLI

Check it from a terminal:

=== "Terminal"

    <!-- termynal -->

    ```bash
    $ nomage my-identifier --check kebab
    ```

=== "Command"

    ```console
    nomage my-identifier --check kebab
    ```

Check will fail with a return code not equal to `0`.

=== "Terminal"

    <!-- termynal -->

    ```bash
    $ nomage my-identifier --check snake
    Not matching convention: snake_case / snail_case / pothole_case
    ```

=== "Command"

    ```console
    nomage my-identifier --check snake
    ```
