"""
ADD DOCSTRING
"""
from unittest import TestCase
from unittest.mock import patch
from does_quick_time_occur import does_quick_time_occur


class Test(TestCase):
    @patch('random.randint', return_value=1)
    def test_does_quick_time_occur_True_case(self, _):
        expected = True
        actual = does_quick_time_occur()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)
    def test_does_quick_time_occur_False_lower_bound_case(self, _):
        expected = False
        actual = does_quick_time_occur()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=4)
    def test_does_quick_time_occur_False_upper_bound_case(self, _):
        expected = False
        actual = does_quick_time_occur()
        self.assertEqual(expected, actual)
