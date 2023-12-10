"""
ADD DOCSTRING
"""
from unittest import TestCase
from make_boss import make_boss


class Test(TestCase):
    def test_make_boss(self):
        expected = {"Current HP": 200}
        actual = make_boss()
        self.assertEqual(expected, actual)
