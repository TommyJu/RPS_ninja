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
    # patch is for randomly selecting an enemy's possible move coordinate
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

    @patch('random.choice', side_effect=[[1, 1]])
    def test_enemy_move_south(self, _):
        enemies = [[1, 0]]
        visions = [None]
        board = {(0, 0): "A haunted mansion", (1, 0): "A haunted mansion", (2, 0): "A haunted mansion",
                 (0, 1): "A haunted mansion", (1, 1): "A haunted mansion", (2, 1): "A haunted mansion",
                 (0, 2): "A haunted mansion", (1, 2): "A haunted mansion", (2, 2): "A haunted mansion"}
        expected_enemies = [[1, 1]]
        expected_visions = [[1, 2]]
        enemies_move(enemies, visions, board)
        self.assertEqual(expected_enemies, enemies)
        self.assertEqual(expected_visions, visions)

    @patch('random.choice', side_effect=[[1, 1]])
    def test_enemy_move_west(self, _):
        enemies = [[2, 1]]
        visions = [None]
        board = {(0, 0): "A haunted mansion", (1, 0): "A haunted mansion", (2, 0): "A haunted mansion",
                 (0, 1): "A haunted mansion", (1, 1): "A haunted mansion", (2, 1): "A haunted mansion",
                 (0, 2): "A haunted mansion", (1, 2): "A haunted mansion", (2, 2): "A haunted mansion"}
        expected_enemies = [[1, 1]]
        expected_visions = [[0, 1]]
        enemies_move(enemies, visions, board)
        self.assertEqual(expected_enemies, enemies)
        self.assertEqual(expected_visions, visions)

    @patch('random.choice', side_effect=[[1, 1]])
    def test_enemy_move_east(self, _):
        enemies = [[0, 1]]
        visions = [None]
        board = {(0, 0): "A haunted mansion", (1, 0): "A haunted mansion", (2, 0): "A haunted mansion",
                 (0, 1): "A haunted mansion", (1, 1): "A haunted mansion", (2, 1): "A haunted mansion",
                 (0, 2): "A haunted mansion", (1, 2): "A haunted mansion", (2, 2): "A haunted mansion"}
        expected_enemies = [[1, 1]]
        expected_visions = [[2, 1]]
        enemies_move(enemies, visions, board)
        self.assertEqual(expected_enemies, enemies)
        self.assertEqual(expected_visions, visions)

    @patch('random.choice', side_effect=[[0, 1], [2, 1]])
    def test_enemy_vision_cones_in_start_and_end(self, _):
        enemies = [[0, 2], [2, 0]]
        visions = [[0, 1], [2, 1]]
        board = {(0, 0): "A haunted mansion", (1, 0): "A haunted mansion", (2, 0): "A haunted mansion",
                 (0, 1): "A haunted mansion", (1, 1): "A haunted mansion", (2, 1): "A haunted mansion",
                 (0, 2): "A haunted mansion", (1, 2): "A haunted mansion", (2, 2): "A haunted mansion"}
        expected_enemies = [[0, 1], [2, 1]]
        expected_visions = [None, None]
        enemies_move(enemies, visions, board)
        self.assertEqual(expected_enemies, enemies)
        self.assertEqual(expected_visions, visions)

    @patch('random.choice', side_effect=[[0, 1]])
    def test_enemy_vision_cone_out_of_bounds(self, _):
        enemies = [[1, 1]]
        visions = [[0, 1]]
        board = {(0, 0): "A haunted mansion", (1, 0): "A haunted mansion", (2, 0): "A haunted mansion",
                 (0, 1): "A haunted mansion", (1, 1): "A haunted mansion", (2, 1): "A haunted mansion",
                 (0, 2): "A haunted mansion", (1, 2): "A haunted mansion", (2, 2): "A haunted mansion"}
        expected_enemies = [[0, 1]]
        expected_visions = [None]
        enemies_move(enemies, visions, board)
        self.assertEqual(expected_enemies, enemies)
        self.assertEqual(expected_visions, visions)

    @patch('random.choice', side_effect=[[0, 2], [1, 2]])
    def test_enemy_vision_cone_on_enemy(self, _):
        enemies = [[0, 2], [2, 2]]
        visions = [None, [1, 2]]
        board = {(0, 0): "A haunted mansion", (1, 0): "A haunted mansion", (2, 0): "A haunted mansion",
                 (0, 1): "A haunted mansion", (1, 1): "A haunted mansion", (2, 1): "A haunted mansion",
                 (0, 2): "A haunted mansion", (1, 2): "A haunted mansion", (2, 2): "A haunted mansion"}
        expected_enemies = [[0, 2], [1, 2]]
        expected_visions = [None, [0, 2]]
        enemies_move(enemies, visions, board)
        self.assertEqual(expected_enemies, enemies)
        self.assertEqual(expected_visions, visions)
