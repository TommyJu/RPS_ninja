"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""
from unittest import TestCase
from enemy.enemy_detection import enemy_detection


class Test(TestCase):

    def test_enemy_detection_enemy_detects(self):
        enemies = [[1, 1], [2, 3], [3, 3]]
        vision_cones = [[1, 2], [1, 3], None]
        character = {"X-coordinate": 2, "Y-coordinate": 3, "Current HP": 5, "Attack Level": 0}
        actual = enemy_detection(character, enemies, vision_cones)
        expected = 1
        self.assertEqual(expected, actual)

    def test_enemy_detection_vision_cones_detects(self):
        enemies = [[0, 1], [5, 3], [3, 3]]
        vision_cones = [None, [5, 2], [3, 4]]
        character = {"X-coordinate": 3, "Y-coordinate": 4, "Current HP": 5, "Attack Level": 0}
        actual = enemy_detection(character, enemies, vision_cones)
        expected = 2
        self.assertEqual(expected, actual)

    def test_enemy_detection_does_not_detect(self):
        enemies = [[0, 1], [0, 2], [0, 3]]
        vision_cones = [None, None, None]
        character = {"X-coordinate": 1, "Y-coordinate": 2, "Current HP": 5, "Attack Level": 0}
        actual = enemy_detection(character, enemies, vision_cones)
        expected = None
        self.assertEqual(expected, actual)
