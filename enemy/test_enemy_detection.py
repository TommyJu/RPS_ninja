"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""
from unittest import TestCase
from unittest.mock import patch
from enemy.enemy_detection import enemy_detection


class Test(TestCase):
    @patch('random.choice', return_value='rock')
    @patch('random.randint', side_effect=[10, 0])
    @patch('builtins.input', return_value='rock')
    def test_enemy_detection_enemy_detects(self, _, __, ___):
        enemies = [[1, 1], [2, 3], [3, 3]]
        vision_cones = [[1, 2], [1, 3], None]
        character = {"X-coordinate": 2, "Y-coordinate": 3, "Current HP": 5, "Attack Level": 0}
        enemy_detection(character, enemies, [], vision_cones, [])
        expected_lists = ([[1, 1], [3, 3]], [[1, 2], None])
        actual_lists = (enemies, vision_cones)
        self.assertEqual(expected_lists, actual_lists)

    @patch('random.choice', return_value='rock')
    @patch('random.randint', side_effect=[10, 0])
    @patch('builtins.input', return_value='rock')
    def test_enemy_detection_vision_cones_detects(self, _, __, ___):
        enemies = [[0, 1], [5, 3], [3, 3]]
        vision_cones = [None, [5, 2], [3, 4]]
        character = {"X-coordinate": 3, "Y-coordinate": 4, "Current HP": 5, "Attack Level": 0}
        enemy_detection(character, enemies, [], vision_cones, [])
        expected_lists = ([[0, 1], [5, 3]], [None, [5, 2]])
        actual_lists = (enemies, vision_cones)
        self.assertEqual(expected_lists, actual_lists)

    @patch('random.choice', return_value='rock')
    @patch('random.randint', side_effect=[10, 0])
    @patch('builtins.input', return_value='rock')
    def test_enemy_detection_does_not_detect(self, _, __, ___):
        enemies = [[0, 1], [0, 2], [0, 3]]
        vision_cones = [None, None, None]
        character = {"X-coordinate": 1, "Y-coordinate": 2, "Current HP": 5, "Attack Level": 0}
        enemy_detection(character, enemies, [], vision_cones, [])
        expected_lists = ([[0, 1], [0, 2], [0, 3]], [None, None, None])
        actual_lists = (enemies, vision_cones)
        self.assertEqual(expected_lists, actual_lists)

    @patch('random.choice', side_effect=['rock', 'paper'])
    @patch('random.randint', side_effect=[10, 0, 10, 0])
    @patch('builtins.input', side_effect=['rock', 'paper'])
    def test_enemy_detection_vision_cones_detects_recursion(self, _, __, ___):
        enemies = [[2, 1], [5, 3], [3, 2]]
        vision_cones = [[2, 2], [5, 2], [2, 2]]
        character = {"X-coordinate": 2, "Y-coordinate": 2, "Current HP": 5, "Attack Level": 0}
        enemy_detection(character, enemies, [], vision_cones, [])
        expected_lists = ([[5, 3]], [[5, 2]])
        actual_lists = (enemies, vision_cones)
        self.assertEqual(expected_lists, actual_lists)
