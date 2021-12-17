"""
Lumache - Python library for cooks and food lovers.
"""
import random


__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""
    pass

class FooError(Exception):
    """Raise this error whenever you want."""
    pass


class BarError(Exception):
    """Raise this error whenever you want."""
    pass


def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]
    """
    return ["shells", "gorgonzola", "parsley"]


def foo(x):
    if random.randint(0, 100) % 2 == 0:
        raise FooError()
    return "You passed!"


def bar():
    return str(random.randint(0, 10_000))