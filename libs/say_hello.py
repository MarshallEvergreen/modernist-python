"""Example package to say hello using cowsay."""


import cowsay


def say_hello() -> str:
    """Return a greeting message using cowsay."""

    return str(cowsay.cow('Hello World'))

