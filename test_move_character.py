"""
Tommy Ju
A01347715

Matthew
A01373290
"""
from unittest import TestCase
from move_character import move_character


class TestMoveCharacter(TestCase):
    def test_move_character_north(self):
        actual = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        move_character(actual, "north")
        expected = {"X-coordinate": 0, "Y-coordinate": -1, "Current HP": 5}
        self.assertEqual(actual, expected)

    def test_move_character_south(self):
        actual = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        move_character(actual, "south")
        expected = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
        self.assertEqual(actual, expected)

    def test_move_character_east(self):
        actual = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        move_character(actual, "east")
        expected = {"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 5}
        self.assertEqual(actual, expected)

    def test_move_character_west(self):
        actual = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        move_character(actual, "west")
        expected = {"X-coordinate": -1, "Y-coordinate": 0, "Current HP": 5}
        self.assertEqual(actual, expected)


def main():
    pass


if __name__ == "__main__":
    main()
