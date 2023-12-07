"""
ADD DOCSTRING
"""
from unittest import TestCase
from enemy.make_vision_cones import make_vision_cones
from unittest.mock import patch


class Test(TestCase):

    @patch('random.choice', side_effect=["north", "south", "east", "west"])
    def test_all_vision_cone_generation_directions(self, _):
        board = {(0, 0): "A haunted mansion", (1, 0): "A haunted mansion", (2, 0): "A haunted mansion",
                 (0, 1): "A haunted mansion", (1, 1): "A haunted mansion", (2, 1): "A haunted mansion",
                 (0, 2): "A haunted mansion", (1, 2): "A haunted mansion", (2, 2): "A haunted mansion",
                 (0, 3): "A haunted mansion", (1, 3): "A haunted mansion", (2, 3): "A haunted mansion"}
        enemies = [[2, 3], [0, 0], [1, 0], [2, 1]]
        #           north   south   east    west
        expected = [[2, 2], [0, 1], [2, 0], [1, 1]]
        actual = make_vision_cones(enemies, board)
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=["north", "south", "east", "west"])
    def test_vision_cones_out_of_bounds(self, _):
        board = {(0, 0): "A haunted mansion", (1, 0): "A haunted mansion", (2, 0): "A haunted mansion",
                 (0, 1): "A haunted mansion", (1, 1): "A haunted mansion", (2, 1): "A haunted mansion",
                 (0, 2): "A haunted mansion", (1, 2): "A haunted mansion", (2, 2): "A haunted mansion",
                 (0, 3): "A haunted mansion", (1, 3): "A haunted mansion", (2, 3): "A haunted mansion"}
        enemies = [[1, 0], [1, 3], [2, 1], [0, 1]]
        expected = [None, None, None, None]
        actual = make_vision_cones(enemies, board)
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=["north", "south"])
    def test_vision_cones_on_start_and_end(self, _):
        board = {(0, 0): "A haunted mansion", (1, 0): "A haunted mansion", (2, 0): "A haunted mansion",
                 (0, 1): "A haunted mansion", (1, 1): "A haunted mansion", (2, 1): "A haunted mansion",
                 (0, 2): "A haunted mansion", (1, 2): "A haunted mansion", (2, 2): "A haunted mansion",
                 (0, 3): "A haunted mansion", (1, 3): "A haunted mansion", (2, 3): "A haunted mansion"}
        enemies = [[0, 1], [2, 2]]
        expected = [None, None]
        actual = make_vision_cones(enemies, board)
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=["north", "south"])
    def test_vision_cones_on_enemy(self, _):
        board = {(0, 0): "A haunted mansion", (1, 0): "A haunted mansion", (2, 0): "A haunted mansion",
                 (0, 1): "A haunted mansion", (1, 1): "A haunted mansion", (2, 1): "A haunted mansion",
                 (0, 2): "A haunted mansion", (1, 2): "A haunted mansion", (2, 2): "A haunted mansion",
                 (0, 3): "A haunted mansion", (1, 3): "A haunted mansion", (2, 3): "A haunted mansion"}
        enemies = [[0, 2], [0, 1]]
        expected = [None, None]
        actual = make_vision_cones(enemies, board)
        self.assertEqual(expected, actual)
    # @patch('random.choice', side_effect=['west', 'north', 'north'])
    # def test_make_vision_cone_goes_outside_border(self, _):
    #     enemies1 = [[0, 1], [1, 0], [0, 1]]
    #     expected = [[-1, 1], [1, -1], [0, 0]]
    #     actual = make_vision_cones(enemies1)
    #     self.assertEquals(expected, actual)
    #
    # @patch('random.choice', side_effect=['east', 'south'])
    # def test_make_vision_cone_can_double(self, _):
    #     enemies1 = [[0, 1], [1, 0]]
    #     expected = [[1, 1], [1, 1]]
    #     actual = make_vision_cones(enemies1)
    #     self.assertEquals(expected, actual)
