"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""
from unittest import TestCase
from unittest.mock import patch
from combat.engage_combat import engage_combat


class Test(TestCase):

    @patch('random.choice', return_value='rock')
    @patch('random.randint', side_effect=[3, 0])
    @patch('builtins.input', return_value='rock')
    def test_engage_combat_one_shot_draw(self, _, __, ___):
        character = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5, "Attack Level": 0}
        enemies = [[0, 1], [0, 2], [1, 2]]
        vision_cones = [[1, 1], None, [1, 3]]
        index = 0
        engage_combat(character, enemies, vision_cones, index)
        expected_lists = ([[0, 2], [1, 2]], [None, [1, 3]])
        actual_lists = (enemies, vision_cones)
        expected_hp = 5
        self.assertEqual(expected_lists, actual_lists)
        self.assertEqual(expected_hp, character["Current HP"])

    @patch('random.choice', return_value='scissor')
    @patch('random.randint', side_effect=[3, 0])
    @patch('builtins.input', return_value='rock')
    def test_engage_combat_one_shot_not_draw(self, _, __, ___):
        character = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 4, "Attack Level": 0}
        enemies = [[0, 2], [1, 2], [0, 1]]
        vision_cones = [None, [1, 3], [1, 1]]
        index = 2
        engage_combat(character, enemies, vision_cones, index)
        expected_lists = ([[0, 2], [1, 2]], [None, [1, 3]])
        actual_lists = (enemies, vision_cones)
        expected_hp = 4
        self.assertEqual(expected_lists, actual_lists)
        self.assertEqual(expected_hp, character["Current HP"])

    @patch('random.choice', return_value='rock')
    @patch('random.randint', side_effect=[0, 3])
    @patch('builtins.input', side_effect=['rock'])
    def test_engage_combat_player_dies_one_shot_draw(self, _, __, ___):
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 3, "Attack Level": 0}
        enemies = [[2, 1], [0, 2], [1, 2]]
        vision_cones = [[1, 1], None, None]
        index = 0
        engage_combat(character, enemies, vision_cones, index)
        print(character["Current HP"])
        expected = ([[0, 2], [1, 2]], [None, None])
        actual = (enemies, vision_cones)
        expected_hp = 0
        self.assertEqual(expected, actual)
        self.assertEqual(expected_hp, character["Current HP"])

    @patch('random.choice', return_value='scissor')
    @patch('random.randint', side_effect=[0, 6])
    @patch('builtins.input', side_effect=['paper'])
    def test_engage_combat_player_dies_one_shot_not_draw(self, _, __, ___):
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 6, "Attack Level": 0}
        enemies = [[2, 1], [0, 2], [1, 2]]
        vision_cones = [[1, 1], None, None]
        index = 0
        engage_combat(character, enemies, vision_cones, index)
        print(character["Current HP"])
        expected = ([[0, 2], [1, 2]], [None, None])
        actual = (enemies, vision_cones)
        expected_hp = 0
        self.assertEqual(expected, actual)
        self.assertEqual(expected_hp, character["Current HP"])

    @patch('random.choice', side_effect=['scissor', 'scissor'])
    @patch('random.randint', side_effect=[0, 0, 0, 0])
    @patch('builtins.input', side_effect=['paper', 'paper'])
    def test_engage_combat_player_dies_multi_shot_not_draw(self, _, __, ___):
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 2, "Attack Level": 0}
        enemies = [[2, 1], [0, 2], [1, 2]]
        vision_cones = [[1, 1], None, None]
        index = 0
        engage_combat(character, enemies, vision_cones, index)
        print(character["Current HP"])
        expected = ([[0, 2], [1, 2]], [None, None])
        actual = (enemies, vision_cones)
        expected_hp = 0
        self.assertEqual(expected, actual)
        self.assertEqual(expected_hp, character["Current HP"])

    @patch('random.choice', side_effect=['paper', 'paper'])
    @patch('random.randint', side_effect=[0, 1, 0, 1])
    @patch('builtins.input', side_effect=['paper', 'paper'])
    def test_engage_combat_player_dies_multi_shot_not_draw(self, _, __, ___):
        character = {"X-coordinate": 2, "Y-coordinate": 1, "Current HP": 2, "Attack Level": 0}
        enemies = [[2, 1], [0, 2], [1, 2]]
        vision_cones = [[1, 1], None, None]
        index = 0
        engage_combat(character, enemies, vision_cones, index)
        print(character["Current HP"])
        expected = ([[0, 2], [1, 2]], [None, None])
        actual = (enemies, vision_cones)
        expected_hp = 0
        self.assertEqual(expected, actual)
        self.assertEqual(expected_hp, character["Current HP"])