"""
Tommy Ju
A01347715

Matthew
A01373290
"""
from make_character import make_character
from make_board import make_board
from get_user_choice import get_user_choice
from move_character import move_character
from describe_current_location import describe_current_location


def game():
    rows = 5
    columns = 5
    end_point = (4, 4)
    board = make_board(rows, columns)
    character = make_character()
    achieved_goal = True

    while achieved_goal:
        direction = get_user_choice()
        move_character(character, direction)
        describe_current_location(board, character)


def main():
    game()


if __name__ == "__main__":
    main()
