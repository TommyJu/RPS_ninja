"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""
from unittest import TestCase
from does_player_win import does_player_win


class Test(TestCase):
    def test_does_player_win_draw_case(self):
        expected = 'draw'
        actual = does_player_win(('rock', 8), ('rock', 8))

        self.assertEqual(expected, actual)

    def test_does_player_win_win_case(self):
        expected = True
        actual = does_player_win(('rock', 8), ('scissor', 8))
        self.assertEqual(expected, actual)

    def test_does_player_win_lose_case(self):
        expected = False
        actual = does_player_win(('scissor', 8), ('rock', 8))
        self.assertEqual(expected, actual)
