"""
Tommy Ju
A01347715
"""
from unittest import TestCase
from game import make_character


def main():
    pass


if __name__ == "__main__":
    main()


class TestMakeCharacter(TestCase):
    def test_make_character(self):
        actual = make_character()
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        self.assertEqual(actual, expected)