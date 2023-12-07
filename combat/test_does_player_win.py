"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""
from unittest import TestCase
from does_player_win import does_player_win


class Test(TestCase):

    def test_does_player_win_rock_draw_case_True(self):
        expected = True
        actual = does_player_win(('rock', 9), ('rock', 8))
        self.assertEqual(expected, actual)

    def test_does_player_win_rock_draw_case_True_boundary(self):
        expected = True
        actual = does_player_win(('rock', 8), ('rock', 8))
        self.assertEqual(expected, actual)

    def test_does_player_win_rock_draw_case_False(self):
        expected = False
        actual = does_player_win(('rock', 7), ('rock', 8))
        self.assertEqual(expected, actual)

    def test_does_player_win_rock_win_case(self):
        expected = True
        actual = does_player_win(('rock', 7), ('scissor', 8))
        self.assertEqual(expected, actual)

    def test_does_player_win_rock_lose_case(self):
        expected = False
        actual = does_player_win(('rock', 7), ('paper', 8))
        self.assertEqual(expected, actual)

    def test_does_player_win_scissor_lose_case(self):
        expected = False
        actual = does_player_win(('scissor', 7), ('rock', 8))
        self.assertEqual(expected, actual)

    def test_does_player_win_scissor_draw_case_True(self):
        expected = True
        actual = does_player_win(('scissor', 9), ('scissor', 8))
        self.assertEqual(expected, actual)

    def test_does_player_win_scissor_draw_case_True_boundary(self):
        expected = True
        actual = does_player_win(('scissor', 8), ('scissor', 8))
        self.assertEqual(expected, actual)

    def test_does_player_win_scissor_draw_case_False(self):
        expected = False
        actual = does_player_win(('scissor', 7), ('scissor', 8))
        self.assertEqual(expected, actual)

    def test_does_player_win_scissor_win_case(self):
        expected = True
        actual = does_player_win(('scissor', 7), ('paper', 8))
        self.assertEqual(expected, actual)

    def test_does_player_win_paper_lose_case(self):
        expected = False
        actual = does_player_win(('paper', 7), ('scissor', 8))
        self.assertEqual(expected, actual)

    def test_does_player_win_paper_draw_case_True(self):
        expected = True
        actual = does_player_win(('paper', 9), ('paper', 8))
        self.assertEqual(expected, actual)

    def test_does_player_win_paper_draw_case_True_boundary(self):
        expected = True
        actual = does_player_win(('paper', 8), ('paper', 8))
        self.assertEqual(expected, actual)

    def test_does_player_win_paper_draw_case_False(self):
        expected = False
        actual = does_player_win(('paper', 7), ('paper', 8))
        self.assertEqual(expected, actual)

    def test_does_player_win_paper_win_case(self):
        expected = True
        actual = does_player_win(('paper', 7), ('rock', 8))
        self.assertEqual(expected, actual)


