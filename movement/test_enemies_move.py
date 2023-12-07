"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""
from unittest import TestCase
from movement.enemies_move import enemies_move
from unittest.mock import patch


class Test(TestCase):
    # patch is for randomly selecting an enemy's possible moves
    @patch('random.choice', side_effect=[[1, 1]])
    def test_enemy_move_north(self, _):
        enemies = [[1, 2]]
        visions = [None]
        board = {(0, 0): "A haunted mansion", (1, 0): "A haunted mansion", (2, 0): "A haunted mansion",
                 (0, 1): "A haunted mansion", (1, 1): "A haunted mansion", (2, 1): "A haunted mansion",
                 (0, 2): "A haunted mansion", (1, 2): "A haunted mansion", (2, 2): "A haunted mansion"}
        expected_enemies = [[1, 1]]
        expected_visions = [[1, 0]]
        enemies_move(enemies, visions, board)
        self.assertEqual(expected_enemies, enemies)
        self.assertEqual(expected_visions, visions)


class TestEnemiesMove(TestCase):
    def test_enemies_move(self):
        self.fail()
