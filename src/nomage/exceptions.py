"""
Nomage - exceptions.

This module defines the custom exception types raised by the Nomage Python API.
These exceptions are used to report errors related to unknown or unrecognized
naming convention.
"""


class UnknownNamingConventionError(ValueError):
    """
    Raised when a requested naming convention is not known or not registered.

    This typically occurs when a provided convention name does not match any built-in
    or user-defined naming conventions.

    Attributes:
        nc_name: The naming convention name.
    """

    def __init__(self, nc_name: str) -> None:
        super().__init__(f"could not find naming convention '{nc_name}'")
        self.nc_name = nc_name


class UnrecognizedNamingConventionError(ValueError):
    """
    Raised when an identifier cannot be matched to any known naming convention.

    This indicates that the identifier does not conform to any of the registered
    naming conventions and therefore cannot be reliably detected.

    Attributes:
        id_str: The identifier string.
    """

    def __init__(self, id_str: str) -> None:
        super().__init__(
            f"no matching naming convention, invalid identifier '{id_str}'"
        )
        self.id_str = id_str
