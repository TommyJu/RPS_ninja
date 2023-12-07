"""
Tommy Ju
A01347715

Matthew
A01373290
"""
from unittest import TestCase
from map.describe_current_location import describe_current_location
from unittest.mock import patch
import io


class TestDescribeCurrentLocation(TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_starting_corner(self, mock_stdout):
        game_board = {(0, 0): "A haunted mansion", (1, 0): "A deserted village",
                      (0, 1): "An eerie forest", (1, 1): "A mountain trail"}
        describe_current_location(game_board, {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5})
        expected = "Your location: A haunted mansion (0, 0)\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_final_corner(self, mock_stdout):
        game_board = {(0, 0): "A haunted mansion", (1, 0): "A deserted village",
                      (0, 1): "An eerie forest", (1, 1): "A mountain trail"}
        describe_current_location(game_board, {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5})
        expected = "Your location: A mountain trail (1, 1)\n"
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_middle_board(self, mock_stdout):
        game_board = {(0, 0): "A haunted mansion", (1, 0): "A haunted mansion", (2, 0): "A haunted mansion",
                      (0, 1): "A haunted mansion", (1, 1): "An eerie forest", (2, 1): "A haunted mansion",
                      (0, 2): "A haunted mansion", (1, 2): "A haunted mansion", (2, 2): "A haunted mansion"}
        describe_current_location(game_board, {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5})
        expected = "Your location: An eerie forest (1, 1)\n"
        self.assertEqual(mock_stdout.getvalue(), expected)


def main():
    pass


if __name__ == "__main__":
    main()
