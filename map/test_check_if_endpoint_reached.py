"""
Tommy Ju
A01347715
Matthew
A01373290
"""
from unittest import TestCase
from check_if_endpoint_reached import check_if_endpoint_reached


class Test(TestCase):
    def test_check_if_endpoint_reached_True_case(self):
        character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5, "Attack Level": 0}
        board = {(0, 0): "A haunted mansion", (1, 0): "A deserted village",
                 (0, 1): "An eerie forest", (1, 1): "A mountain trail"}
        actual = check_if_endpoint_reached(character, board)
        expected = False
        self.assertEqual(expected, actual)

    def test_check_if_endpoint_reached_False_case(self):
        character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5, "Attack Level": 0}
        board = {(0, 0): "A haunted mansion", (1, 0): "A haunted mansion",
                 (0, 1): "An eerie forest", (1, 1): "A mountain trail"}
        actual = check_if_endpoint_reached(character, board)
        expected = True
        self.assertEqual(expected, actual)
