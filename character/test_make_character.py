"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""
from unittest import TestCase
from character.make_character import make_character


class TestMakeCharacter(TestCase):
    def test_make_character(self):
        actual = make_character()
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Attack Level": 0}
        self.assertEqual(actual, expected)

