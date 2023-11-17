"""
Tommy Ju
A01347715

Matthew
A01373290
"""


from unittest import TestCase
from get_user_choice import get_user_choice
import io
from unittest.mock import patch


class TestGetUserChoice(TestCase):
    # Testing movement north
    @patch("builtins.input", side_effect=["north"])
    def test_north(self, _):
        actual = get_user_choice()
        expected = "north"
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=["n"])
    def test_n(self, _):
        actual = get_user_choice()
        expected = "north"
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=["1"])
    def test_1(self, _):
        actual = get_user_choice()
        expected = "north"
        self.assertEqual(actual, expected)

    # Testing movement south
    @patch("builtins.input", side_effect=["south"])
    def test_south(self, _):
        actual = get_user_choice()
        expected = "south"
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=["s"])
    def test_s(self, _):
        actual = get_user_choice()
        expected = "south"
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=["2"])
    def test_2(self, _):
        actual = get_user_choice()
        expected = "south"
        self.assertEqual(actual, expected)

    # Testing movement east
    @patch("builtins.input", side_effect=["east"])
    def test_east(self, _):
        actual = get_user_choice()
        expected = "east"
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=["e"])
    def test_e(self, _):
        actual = get_user_choice()
        expected = "east"
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=["3"])
    def test_3(self, _):
        actual = get_user_choice()
        expected = "east"
        self.assertEqual(actual, expected)

    # Testing movement west
    @patch("builtins.input", side_effect=["west"])
    def test_west(self, _):
        actual = get_user_choice()
        expected = "west"
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=["w"])
    def test_w(self, _):
        actual = get_user_choice()
        expected = "west"
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=["4"])
    def test_4(self, _):
        actual = get_user_choice()
        expected = "west"
        self.assertEqual(actual, expected)

    # Testing 3 kinds of invalid input
    @patch("builtins.input", side_effect=["feaw", "west"])
    def test_invalid_text_return_value(self, _):
        actual = get_user_choice()
        expected = "west"
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=["eafg", "west"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_invalid_text_print(self, mock_stdout, _):
        get_user_choice()
        expected = ("\nPlease enter a valid direction.\n"
                    "To move north: type 'north', 'n', or '1'\n")
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch("builtins.input", side_effect=["z", "west"])
    def test_invalid_letter_return_value(self, _):
        actual = get_user_choice()
        expected = "west"
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=["z", "west"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_invalid_letter_print(self, mock_stdout, _):
        get_user_choice()
        expected = ("\nPlease enter a valid direction.\n"
                    "To move north: type 'north', 'n', or '1'\n")
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch("builtins.input", side_effect=["8", "west"])
    def test_invalid_number_return_value(self, _):
        actual = get_user_choice()
        expected = "west"
        self.assertEqual(actual, expected)

    @patch("builtins.input", side_effect=["8", "west"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_invalid_number_print(self, mock_stdout, _):
        get_user_choice()
        expected = ("\nPlease enter a valid direction.\n"
                    "To move north: type 'north', 'n', or '1'\n")
        self.assertEqual(mock_stdout.getvalue(), expected)


def main():
    pass


if __name__ == "__main__":
    main()
