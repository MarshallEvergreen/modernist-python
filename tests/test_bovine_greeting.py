"""Test for bovine_greeting library."""



from libs.bovine_greeting.core import say_hello


class TestBovineGreeting:
    def test_sanity(self) -> None:
        assert say_hello() is not None