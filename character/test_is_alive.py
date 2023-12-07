from unittest import TestCase
from character.is_alive import is_alive


class Test(TestCase):
    def test_is_alive_True(self):
        expected = True
        actual = is_alive({"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 5})
        self.assertEqual(expected, actual)

    def test_is_alive_True_lower_boundary(self):
        expected = True
        actual = is_alive({"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 1})
        self.assertEqual(expected, actual)

    def test_is_alive_False(self):
        expected = False
        actual = is_alive({"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 0})
        self.assertEqual(expected, actual)
