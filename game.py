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
# GUI Modules
import tkinter as tk
from PIL import Image, ImageTk
from get_user_interface_data import get_user_interface_data
from user_interface import user_interface
import threading




def game():



    rows = 10
    columns = 10
    end_point = (4, 4)
    board = make_board(rows, columns)
    character = make_character()
    achieved_goal = True
    # GUI


    data = get_user_interface_data(character, end_point, [(2, 2), (1, 1)])
    root = tk.Tk()
    user_interface(root, rows, columns, data)
    game_thread = threading.Thread(target=game_instance, args=(root, character, achieved_goal, board, end_point, rows, columns)).start()
    root.after(100, game_thread)
    root.mainloop()


def game_instance(root, character, achieved_goal, board, end_point, rows, columns):
    while achieved_goal:
        direction = get_user_choice()
        move_character(character, direction)
        describe_current_location(board, character)
        data = get_user_interface_data(character, end_point, [(2, 2), (1, 1)])
        user_interface(root, rows, columns, data)
        root.update()

def main():
    game()


if __name__ == "__main__":
    main()
