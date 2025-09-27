"""Example package to say hello using cowsay."""

from cowsay import say


def say_hello() -> str:
    """Return a greeting message using cowsay."""

    hey = say("Hello World")
    return hey
