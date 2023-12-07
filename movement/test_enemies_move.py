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

    @patch('random.choice', side_effect=[[1, 1], [1, 2]])
    def test_enemies_move_both_move_south(self, _):
        enemies = [[0, 1], [0, 2]]
        visions = [[1, 1], [1, 2]]
        board = {(0, 0): 'string', (0, 1): 'string', (0, 2): 'string',
                 (1, 0): 'string', (1, 1): 'string', (1, 2): 'string'}
        expected_enemies = [[1, 1], [1, 2]]
        expected_visions = [[2, 1], [2, 2]]
        actual = enemies_move(enemies, visions, board)
        self.assertEqual(expected_enemies, enemies)
        self.assertEqual(expected_visions, visions)
