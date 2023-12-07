"""
Tommy Ju
A01347715

Matthew
A01373290
"""
from unittest import TestCase
from unittest.mock import patch
from map.make_board import make_board


class TestMakeBoard(TestCase):
    @patch("random.choice", side_effect=["A haunted mansion", "An eerie forest",
                                         "A deserted village", "A mountain trail"])
    def test_smallest_board(self, _):
        actual = make_board(2, 2)
        expected = {(0, 0): "A haunted mansion", (1, 0): "A deserted village",
                    (0, 1): "An eerie forest", (1, 1): "A mountain trail"}
        self.assertEqual(actual, expected)

    @patch("random.choice", side_effect=["A haunted mansion", "A haunted mansion",
                                         "A haunted mansion", "A haunted mansion",
                                         "A haunted mansion", "A haunted mansion"])
    def test_rectangular_board(self, _):
        actual = make_board(2, 3)
        expected = {(0, 0): "A haunted mansion", (1, 0): "A haunted mansion",
                    (0, 1): "A haunted mansion", (1, 1): "A haunted mansion",
                    (0, 2): "A haunted mansion", (1, 2): "A haunted mansion"}
        self.assertEqual(actual, expected)

    @patch("random.choice", side_effect=["A haunted mansion"]*9)
    def test_normal_square_board(self, _):
        actual = make_board(3, 3)
        expected = {(0, 0): "A haunted mansion", (1, 0): "A haunted mansion", (2, 0): "A haunted mansion",
                    (0, 1): "A haunted mansion", (1, 1): "A haunted mansion", (2, 1): "A haunted mansion",
                    (0, 2): "A haunted mansion", (1, 2): "A haunted mansion", (2, 2): "A haunted mansion"}
        self.assertEqual(actual, expected)


def main():
    pass


if __name__ == "__main__":
    main()
