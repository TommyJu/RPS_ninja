"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""
from unittest import TestCase
from unittest.mock import patch
from random_enemy_action import random_enemy_action


class Test(TestCase):

    @patch('random.choice', return_value='scissor')
    @patch('random.randint', return_value=10)
    def test_enemy_action_scissor_highest_power(self, _, __):
        expected = ('scissor', 10)
        actual = random_enemy_action()

    @patch('random.choice', return_value='scissor')
    @patch('random.randint', return_value=0)
    def test_enemy_action_scissor_lowest_power(self, _, __):
        expected = ('scissor', 0)
        actual = random_enemy_action()

    @patch('random.choice', return_value='paper')
    @patch('random.randint', return_value=10)
    def test_enemy_action_paper_highest_power(self, _, __):
        expected = ('paper', 10)
        actual = random_enemy_action()

    @patch('random.choice', return_value='paper')
    @patch('random.randint', return_value=0)
    def test_enemy_action_paper_lowest_power(self, _, __):
        expected = ('paper', 0)
        actual = random_enemy_action()

    @patch('random.choice', return_value='rock')
    @patch('random.randint', return_value=10)
    def test_enemy_action_rock_highest_power(self, _, __):
        expected = ('rock', 10)
        actual = random_enemy_action()

    @patch('random.choice', return_value='rock')
    @patch('random.randint', return_value=0)
    def test_enemy_action_rock_highest_power(self, _, __):
        expected = ('rock', 0)
        actual = random_enemy_action()
