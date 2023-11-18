from unittest import TestCase
from validate_move import validate_move


class Test(TestCase):

    def test_validate_move_north_invalid_move(self):
        character_1 = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        board_1 = {(0, 0): 'Empty room', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room'}
        user_input_1 = 'north'
        expected = False
        actual = validate_move(board_1, character_1, user_input_1)
        self.assertEqual(expected, actual)

    def test_validate_move_north_valid_move(self):
        character_1 = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
        board_1 = {(0, 0): 'Empty room', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room'}
        user_input_1 = 'north'
        expected = True
        actual = validate_move(board_1, character_1, user_input_1)
        self.assertEqual(expected, actual)

    def test_validate_move_east_invalid_move(self):
        character_1 = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
        board_1 = {(0, 0): 'Empty room', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room'}
        user_input_1 = 'east'
        expected = False
        actual = validate_move(board_1, character_1, user_input_1)
        self.assertEqual(expected, actual)

    def test_validate_move_east_valid_move(self):
        character_1 = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
        board_1 = {(0, 0): 'Empty room', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room'}
        user_input_1 = 'east'
        expected = True
        actual = validate_move(board_1, character_1, user_input_1)
        self.assertEqual(expected, actual)

    def test_validate_move_west_invalid_move(self):
        character_1 = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
        board_1 = {(0, 0): 'Empty room', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room'}
        user_input_1 = 'west'
        expected = False
        actual = validate_move(board_1, character_1, user_input_1)
        self.assertEqual(expected, actual)

    def test_validate_move_west_valid_move(self):
        character_1 = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
        board_1 = {(0, 0): 'Empty room', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room'}
        user_input_1 = 'west'
        expected = True
        actual = validate_move(board_1, character_1, user_input_1)
        self.assertEqual(expected, actual)

    def test_validate_move_south_invalid_move(self):
        character_1 = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 3}
        board_1 = {(0, 0): 'Empty room', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room'}
        user_input_1 = 'south'
        expected = False
        actual = validate_move(board_1, character_1, user_input_1)
        self.assertEqual(expected, actual)

    def test_validate_move_south_valid_move(self):
        character_1 = {"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 4}
        board_1 = {(0, 0): 'Empty room', (0, 1): 'Empty room', (1, 0): 'Empty room', (1, 1): 'Empty room'}
        user_input_1 = 'south'
        expected = True
        actual = validate_move(board_1, character_1, user_input_1)
        self.assertEqual(expected, actual)

    def test_validate_move_single_room_case(self):
        character_1 = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 4}
        board_1 = {(0, 0): 'Empty room'}
        user_input_1 = 'south'
        expected = False
        actual = validate_move(board_1, character_1, user_input_1)
        self.assertEqual(expected, actual)