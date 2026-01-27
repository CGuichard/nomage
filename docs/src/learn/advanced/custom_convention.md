# Custom convention

While the [built-in naming conventions](../conventions.md) may cover the majority of
use cases, Nomage also allows you to define and use your own custom naming conventions.
This is useful when working with project‑specific rules or non-standard identifier formats.

Custom conventions are only available through the Python API and are not supported
by the command-line interface.

## Overview

A custom naming convention defines how an identifier:

- Is **recognized** (matching).
- Is **parsed** into logical components.
- Is **reconstructed** (converted) from those components.

These responsibilities are encapsulated in the `NamingConvention` class.

## Defining a custom convention

A custom convention is created by instantiating `NamingConvention` with the following elements:

- **`names`** -
  One or more names used to reference the naming convention.

- **`match_regex`** -
  A regular expression used to determine whether an identifier matches the convention.

- **`parser`** -
  A callable that converts a matching identifier string into a tuple of components.

- **`converter`** -
  A callable that converts a tuple of components back into a string representation.

The example below defines a `point.case` convention, where identifier components
are separated by dots.

```python
import re

from nomage import NamingConvention, naming

custom_nc = NamingConvention(
    names=("point.case", "dot.case"),
    match_regex=re.compile(r"^[a-z][a-z0-9]*(\.[a-z][a-z0-9]*)*$"),
    parser=lambda id_str: tuple(id_str.lower().split(".")),
    converter=lambda components: ".".join(components),
)
```

!!! tip
    Review the [`NamingConvention`](../../reference/api/nomage/convention.md#nomage.convention.NamingConvention)
    API Reference to learn more about it.

## Using a custom convention

Custom conventions can be passed explicitly when calling
[`naming`](../../reference/api/nomage/naming.md#nomage.naming.naming).
This allows Nomage to recognize and operate on identifiers using the custom rules.

```python
custom_test_id = naming("test.identifier", conventions=[custom_nc])
```

Once created, identifiers can be converted to any other available convention,
including built-in ones:

```python
pascal_test_id = custom_test_id.to("pascal")
```

Converted identifiers can also be converted back to the custom convention:

```python
new_custom_test_id = naming(pascal_test_id).to(custom_nc)
```

```python
assert str(custom_test_id) != str(pascal_test_id)
assert str(custom_test_id) == str(new_custom_test_id)
```

## Key concepts

- **Detection** relies on the provided regular expression.
- **Parsing** must be deterministic and reversible.
- **Conversion** should preserve semantic components across formats.

As long as these rules are respected, custom conventions integrate seamlessly with built-in ones.

## Limitations

- Custom conventions are only supported via the Python API.
- They must be explicitly provided when ambiguity exists.
- Incorrect or overly permissive regular expressions may lead to unexpected matches.
