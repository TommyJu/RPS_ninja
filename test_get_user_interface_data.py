"""
Tommy Ju
A01347715
"""
from unittest import TestCase
from get_user_interface_data import get_user_interface_data


def main():
    pass


if __name__ == "__main__":
    main()


class TestGetUserInterfaceData(TestCase):
    def test_no_enemies(self):
        expected = {'character': (1, 1), 'endpoint': (4, 4), 'enemies': []}
        actual = get_user_interface_data(
            {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5},
            (4, 4),
            []
        )
        self.assertEqual(actual, expected)

    def test_one_enemy(self):
        expected = {'character': (1, 2), 'endpoint': (0, 4), 'enemies': [(3, 3)]}
        actual = get_user_interface_data(
            {"X-coordinate": 1, "Y-coordinate": 2, "Current HP": 5},
            (0, 4),
            [(3, 3)]
        )
        self.assertEqual(actual, expected)

    def test_multiple_enemies(self):
        expected = {'character': (3, 3), 'endpoint': (4, 0), 'enemies': [(3, 3), (2, 1), (1, 1), (4, 0)]}
        actual = get_user_interface_data(
            {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 0},
            (4, 0),
            [(3, 3), (2, 1), (1, 1), (4, 0)]
        )
        self.assertEqual(actual, expected)
        