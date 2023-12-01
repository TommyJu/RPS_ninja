"""
Tommy Ju
A01347715

Matthew
A01373290
"""
from unittest import TestCase
from unittest.mock import patch

from make_enemy import make_enemy



class Test(TestCase):

    @patch('random.choice', side_effect=[(0, 1), (1, 0)])
    def test_make_enemy_not_in_starting_coordinate(self, _):
        board1 = {(0, 0): 'Empty room', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room'}
        expected = [[0, 1], [1, 0]]
        actual = make_enemy(board1)
        self.assertEquals = (expected, actual)

    @patch('random.choice', side_effect=[(0, 1)])
    def test_make_enemy_round_down_minimum_amount_of_enemy(self, _):
        board2 = {(0, 0): 'Empty room', (0, 1): 'Empty room', (1, 0): 'Empty room', }
        expected = [[0, 1]]
        actual = make_enemy(board2)
        self.assertEquals = (expected, actual)

    @patch('random.choice', side_effect=[(0, 1)])
    def test_make_enemy_1_enemy(self, _):
        board3 = {(0, 0): 'Empty room', (0, 1): 'Empty room'}
        expected = [[0, 1]]
        actual = make_enemy(board3)
        self.assertEquals = (expected, actual)

    @patch('random.choice', side_effect=[(1, 0), (1, 2), (2, 0), (2, 1)])
    def test_make_enemy_multiple_enemies(self, _):
        board4 = {(0, 0): 'Empty room', (0, 1): 'Empty room', (0, 2): 'Empty room', (1, 0): 'Empty room',
                  (1, 1): 'Empty room', (1, 2): 'Empty room', (2, 0): 'Empty room', (2, 1): 'Empty room'}
        expected = [[1, 0]]
        actual = make_enemy(board4)
        self.assertEquals = (expected, actual)
