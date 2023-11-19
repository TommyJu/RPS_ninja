"""
ADD DOCSTRING
"""
from unittest import TestCase
from unittest.mock import patch
from get_choice_combat import get_choice_combat



class Test(TestCase):


    @patch('builtins.input', side_effect=['1'])
    def test_get_choice_combat_correct_input_rock_using_number(self, _):
        expected = 'rock'
        actual = get_choice_combat()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['r'])
    def test_get_choice_combat_correct_input_rock_using_letter(self, _):
        expected = 'rock'
        actual = get_choice_combat()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['rock'])
    def test_get_choice_combat_correct_input_rock_using_word(self, _):
        expected = 'rock'
        actual = get_choice_combat()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['2'])
    def test_get_choice_combat_correct_input_paper_using_number(self, _):
        expected = 'paper'
        actual = get_choice_combat()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['p'])
    def test_get_choice_combat_correct_input_paper_using_letter(self, _):
        expected = 'paper'
        actual = get_choice_combat()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['paper'])
    def test_get_choice_combat_correct_input_paper_using_word(self, _):
        expected = 'paper'
        actual = get_choice_combat()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['3'])
    def test_get_choice_combat_correct_input_scissor_using_number(self, _):
        expected = 'scissor'
        actual = get_choice_combat()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['s'])
    def test_get_choice_combat_correct_input_scissor_using_letter(self, _):
        expected = 'scissor'
        actual = get_choice_combat()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['scissor'])
    def test_get_choice_combat_correct_input_scissor_using_word(self, _):
        expected = 'scissor'
        actual = get_choice_combat()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['S'])
    def test_get_choice_combat_uppercase_correct_input_scissor_using_letter(self, _):
        expected = 'scissor'
        actual = get_choice_combat()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['R'])
    def test_get_choice_combat_uppercase_correct_input_rock_using_letter(self, _):
        expected = 'rock'
        actual = get_choice_combat()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['P'])
    def test_get_choice_combat_uppercase_correct_input_paper_using_letter(self, _):
        expected = 'paper'
        actual = get_choice_combat()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['PaPeR'])
    def test_get_choice_combat_mixedcase_correct_input_paper_using_word(self, _):
        expected = 'paper'
        actual = get_choice_combat()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['rOCk'])
    def test_get_choice_combat_mixedcase_correct_input_rock_using_word(self, _):
        expected = 'rock'
        actual = get_choice_combat()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['sCIssOR'])
    def test_get_choice_combat_mixedcase_correct_input_scissor_using_word(self, _):
        expected = 'scissor'
        actual = get_choice_combat()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['   paper  '])
    def test_get_choice_combat_striptest_correct_input_paper_using_word(self, _):
        expected = 'paper'
        actual = get_choice_combat()
        self.assertEqual(expected, actual)
    @patch('builtins.input', side_effect=['   rock  '])
    def test_get_choice_combat_striptest_correct_input_rock_using_word(self, _):
        expected = 'rock'
        actual = get_choice_combat()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['   scissor  '])
    def test_get_choice_combat_striptest_correct_input_scissor_using_word(self, _):
        expected = 'scissor'
        actual = get_choice_combat()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['   p  '])
    def test_get_choice_combat_striptest_correct_input_paper_using_letter(self, _):
        expected = 'paper'
        actual = get_choice_combat()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['   r  '])
    def test_get_choice_combat_striptest_correct_input_rock_using_letter(self, _):
        expected = 'rock'
        actual = get_choice_combat()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['   s  '])
    def test_get_choice_combat_striptest_correct_input_scissor_using_letter(self, _):
        expected = 'scissor'
        actual = get_choice_combat()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['   1  '])
    def test_get_choice_combat_striptest_correct_input_rock_using_number(self, _):
        expected = 'rock'
        actual = get_choice_combat()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['   2  '])
    def test_get_choice_combat_striptest_correct_input_paper_using_number(self, _):
        expected = 'paper'
        actual = get_choice_combat()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['   3  '])
    def test_get_choice_combat_striptest_correct_input_scissor_using_number(self, _):
        expected = 'scissor'
        actual = get_choice_combat()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['0', '4', '5', '6', '7', '8', '9', '10', ' 11', '13', '99', '123', '2'])
    def test_get_choice_combat_incorrect_loop_input_paper_using_number(self, _):
        expected = 'paper'
        actual = get_choice_combat()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['o', 'i', 'u', 'y', 't', 'e', 'w', 'q', ' a', 'z', 'm', 'n',
                                          'b', 'v', 'c', 'x', 'l', 'k', 'j', 'h', 'g', 'f', 'd', '1'])
    def test_get_choice_combat_incorrect_loop_input_rock_using_letter(self, _):
        expected = 'rock'
        actual = get_choice_combat()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=['rocks', 'papers', 'scissors', 'kaka', 'MaTTHew', 'TOMMY', 'SCISSOR'])
    def test_get_choice_combat_incorrect_loop_input_paper_using_words(self, _):
        expected = 'scissor'
        actual = get_choice_combat()
        self.assertEqual(expected, actual)
