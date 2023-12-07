"""
Tommy Ju
A01347715

Matthew
A01373290
"""
from unittest import TestCase
from validate_move_enemy import validate_move_enemy


class Test(TestCase):
    def test_enemy_at_game_board_lower_bounds(self):
        board = {(0, 0): "A haunted mansion", (1, 0): "A haunted mansion", (2, 0): "A haunted mansion",
                 (0, 1): "A haunted mansion", (1, 1): "A haunted mansion", (2, 1): "A haunted mansion",
                 (0, 2): "A haunted mansion", (1, 2): "A haunted mansion", (2, 2): "A haunted mansion"}
        enemy = [0, 0]
        expected = [[0, 1], [1, 0]]
        actual = validate_move_enemy(enemy, board, [])
        self.assertEqual(expected, actual)

    def test_enemy_at_game_board_upper_bounds(self):
        board = {(0, 0): "A haunted mansion", (1, 0): "A haunted mansion", (2, 0): "A haunted mansion",
                 (0, 1): "A haunted mansion", (1, 1): "A haunted mansion", (2, 1): "A haunted mansion",
                 (0, 2): "A haunted mansion", (1, 2): "A haunted mansion", (2, 2): "A haunted mansion"}
        enemy = [2, 2]
        expected = [[1, 2], [2, 1]]
        actual = validate_move_enemy(enemy, board, [])
        self.assertEqual(expected, actual)

    def test_enemy_beside_other_enemies(self):
        board = {(0, 0): "A haunted mansion", (1, 0): "A haunted mansion", (2, 0): "A haunted mansion",
                 (0, 1): "A haunted mansion", (1, 1): "A haunted mansion", (2, 1): "A haunted mansion",
                 (0, 2): "A haunted mansion", (1, 2): "A haunted mansion", (2, 2): "A haunted mansion"}
        enemy = [1, 1]
        expected = [[0, 1], [1, 0]]
        actual = validate_move_enemy(enemy, board, [[1, 2], [2, 1]])
        self.assertEqual(expected, actual)
