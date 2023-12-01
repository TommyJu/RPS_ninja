"""
Tommy Ju
A01347715
"""
from unittest import TestCase
from make_character import make_character


class TestMakeCharacter(TestCase):
    def test_make_character(self):
        actual = make_character()
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5, "Attack Level": 0}
        self.assertEqual(actual, expected)


def main():
    pass


if __name__ == "__main__":
    main()
