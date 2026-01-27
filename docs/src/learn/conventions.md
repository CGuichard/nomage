# Built-in conventions

Nomage comes with well-known built-in [naming conventions :octicons-link-external-24:](https://en.wikipedia.org/wiki/Naming_convention_(programming)){ target="_blank" }.

| Formatting | Name(s) |
| ---------- | ------- |
|`twowords`  | flatcase, lowercase |
|`TWOWORDS`  | UPPERCASE, SCREAMINGCASE |
|`twoWords`  | camelCase, dromedaryCase |
|`TwoWords`  | PascalCase, UpperCamelCase, StudlyCase |
|`two_words` | snake_case, snail_case, pothole_case |
|`TWO_WORDS` | ALL_CAPS, SCREAMING_SNAKE_CASE, MACRO_CASE, CONSTANT_CASE, ENV_VAR_CASE |
|`two_Words` | camel_Snake_Case |
|`two-words` | kebab-case, dash-case, lisp-case, spinal-case |
|`TWO-WORDS` | COBOL-CASE, SCREAMING-TRAIN-CASE |
|`Two-Words` | Train-Case, Http-Header-Case |

## Python API

When using the built-in conventions from [`builtins_conventions`](../reference/api/nomage/__init__.md#nomage.builtins_conventions)
the mapping key access is really lenient with the name requested.

```python
from nomage import builtins_conventions
conventions = builtins_conventions()

# All of these works
conventions.get("Http-Header-Case")
conventions.get("Http-Header")
conventions.get("http-header")
conventions.get("http_header")
conventions.get("http header")
conventions.get("httpheader")
```

Here are the rules:

- Upper/Capitalize case are ignored.
- The "case" word is ignored.
- Separators "_" and "-" are ignored.
- Space can be used, has it is ignored.
