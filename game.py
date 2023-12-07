"""
Tommy Ju
A01347715

Matthew
A01373290
"""
# Modules created by Matthew and Tommy
from character.make_character import make_character
from map.make_board import make_board
from movement.get_user_choice import get_user_choice
from movement.move_character import move_character
from map.describe_current_location import describe_current_location
from Unused.get_user_interface_data import get_user_interface_data
from enemy.make_enemy import make_enemy
from movement.enemies_move import enemies_move
from enemy.make_vision_cones import make_vision_cones

# GUI Modules
import tkinter as tk
from PIL import Image, ImageTk
import threading


def game():
    rows = 10
    columns = 10
    end_point = (9, 9)
    board = make_board(rows, columns)
    character = make_character()
    enemies = make_enemy(board)
    vision_cones = make_vision_cones(enemies, board)
    achieved_goal = True
    # GUI

    GUI_HEIGHT = 600
    GUI_WIDTH = 1000
    CELL_SIZE = 50

    # Configure the root window
    root = tk.Tk()
    root.title("RPS Ninja")
    root.geometry(f"{GUI_WIDTH}x{GUI_HEIGHT}")
    root.configure(background='black')
    # Root window comprised of 2 vertical columns for map and information
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=2)

    canvas = tk.Canvas(root)
    canvas.grid(row=0, column=0, sticky="nsew")

    # Configure a grid and add data to cells
    for row in range(rows):
        # Configure even rows
        canvas.grid_rowconfigure(row, minsize=CELL_SIZE)
        for column in range(columns):
            # Configure even columns
            canvas.grid_columnconfigure(column, minsize=CELL_SIZE)
            # Add the frame container widget to each cell to create border effect
            frame = tk.Frame(canvas, background="green", borderwidth=3, relief="raised")
            frame.grid(row=row, column=column, sticky="nsew", padx=2, pady=2)

    # Images
    ninja_image_file = Image.open("./assets/ninja-heroic-stance.png")
    ninja_image = ImageTk.PhotoImage(ninja_image_file.resize((30, 30)))
    enemy_image_file = Image.open("./assets/oni.png")
    enemy_image = ImageTk.PhotoImage(enemy_image_file.resize((30, 30)))
    vision_cone_image_file = Image.open("./assets/lantern.png")
    vision_cone_image = ImageTk.PhotoImage(vision_cone_image_file.resize((30, 30)))
    level_one_image_file = Image.open("./assets/forest_level_background.jpeg")
    level_one_image = ImageTk.PhotoImage(level_one_image_file.resize((2000, 2000)))

    #widgets
    all_game_widgets = []
    ninja_widget = tk.Label(canvas, image=ninja_image, background="white")
    enemy_widgets = []
    vision_cone_widgets = []

    # Create widgets
    for index in range(len(enemies)):
        enemy_widget = tk.Label(canvas, image=enemy_image, background="white")
        enemy_widgets.append(enemy_widget)
    for index in range(len(vision_cones)):
        vision_cone_widget = tk.Label(canvas, image=vision_cone_image, background="white")
        vision_cone_widgets.append(vision_cone_widget)

    # Initial game board update
    data = get_user_interface_data(character, end_point, [(2, 2), (1, 1)])
    # Add background image to canvas
    canvas.create_image(0, 0, image=level_one_image)


    def update_widgets(user_interface_data):
        canvas.create_image(0, 0, image=level_one_image)
        ninja_widget.grid(row=user_interface_data["character"][1], column=user_interface_data["character"][0])
        for index in range(len(enemies)):
            enemy_widgets[index].grid(row=enemies[index][1], column=enemies[index][0])
        for index in range(len(vision_cones)):
            if vision_cones[index] == None:
                vision_cone_widgets[index].grid_forget()
            else:
                vision_cone_widgets[index].grid(row=vision_cones[index][1], column=vision_cones[index][0])

    update_widgets(data)


    def game_instance():
        while achieved_goal:
            direction = get_user_choice()
            move_character(character, direction)
            enemies_move(enemies, vision_cones, board)
            describe_current_location(board, character)
            instance_data = get_user_interface_data(character, end_point, [(2, 2), (1, 1)])
            update_widgets(instance_data)


    # Create a separate thread for the game loop
    threading.Thread(target=game_instance).start()
    root.mainloop()


def main():
    game()


if __name__ == "__main__":
    main()
