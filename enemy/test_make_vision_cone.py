"""
ADD DOCSTRING
"""
from unittest import TestCase
from enemy.make_vision_cone import make_vision_cone
from unittest.mock import patch


class Test(TestCase):

    @patch('random.choice', side_effect=['east', 'north', 'north'])
    def test_make_vision_cone_normal_course(self, _):
        enemies1 = [[0, 1], [0, 2], [0, 3]]
        expected = [[1, 1], [0, 1], [0, 2]]
        actual = make_vision_cone(enemies1)
        self.assertEquals(expected, actual)

    @patch('random.choice', side_effect=['west', 'north', 'north'])
    def test_make_vision_cone_goes_outside_border(self, _):
        enemies1 = [[0, 1], [1, 0], [0, 1]]
        expected = [[-1, 1], [1, -1], [0, 0]]
        actual = make_vision_cone(enemies1)
        self.assertEquals(expected, actual)

    @patch('random.choice', side_effect=['east', 'south'])
    def test_make_vision_cone_can_double(self, _):
        enemies1 = [[0, 1], [1, 0]]
        expected = [[1, 1], [1, 1]]
        actual = make_vision_cone(enemies1)
        self.assertEquals(expected, actual)
