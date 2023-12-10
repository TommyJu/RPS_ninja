"""
ADD DOCSTRING
"""
from unittest import TestCase
from restore_hp import restore_hp


class Test(TestCase):
    def test_make_character_normal_course(self):
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 50, "Attack Level": 0, "Max HP": 60}
        actual = restore_hp(character)
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 60, "Attack Level": 0, "Max HP": 60}
        self.assertEqual(actual, expected)

    def test_make_character_same_values(self):
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 60, "Attack Level": 0, "Max HP": 60}
        actual = restore_hp(character)
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 60, "Attack Level": 0, "Max HP": 60}
        self.assertEqual(actual, expected)

    def test_make_character_lower_bound(self):
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 1, "Attack Level": 0, "Max HP": 60}
        actual = restore_hp(character)
        expected = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 60, "Attack Level": 0, "Max HP": 60}
        self.assertEqual(actual, expected)
