"""
ADD DOCSTRING
"""
from unittest import TestCase
from make_vision_cone import make_vision_cone
from unittest.mock import patch


class Test(TestCase):

    @patch('random.choice', side_effect=['east', 'north', 'north'])
    def test_make_vision_cone_normal_course(self, _):
        enemies1 = [[0, 1], [0, 2], [0, 3]]
        expected = [[1, 1], [0, 1], [0, 2]]
        actual = make_vision_cone(enemies1)
        self.assertEquals(expected, actual)

    @patch('random.choice', side_effect=['east', 'north', 'north'])
    def test_make_vision_cone_hits(self, _):
        enemies1 = [[0, 1], [0, 2], [0, 3]]
        expected = [[1, 1], [0, 1], [0, 2]]
        actual = make_vision_cone(enemies1)
        self.assertEquals(expected, actual)
