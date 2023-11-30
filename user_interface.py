"""
Tommy Ju
A01347715

Matthew
A01373290
"""
import tkinter as tk
from PIL import Image, ImageTk
from get_user_interface_data import get_user_interface_data

# Sample data for testing GUI
# some_user_interface_data = get_user_interface_data(
#             {"X-coordinate": 1, "Y-coordinate": 3, "Current HP": 5},
#             (4, 0),
#             [(3, 3), (2, 1), (1, 1), (4, 0)]
#         )

# number_of_rows = 10
# number_of_columns = 10
#
# GUI_HEIGHT = 600
# GUI_WIDTH = 1000
# CELL_SIZE = 50


# This function configures the root
def user_interface(root, rows, columns, user_interface_data):
    # GUI sizing
    GUI_HEIGHT = 600
    GUI_WIDTH = 1000
    CELL_SIZE = 50

    # Configure the root window
    # root = tk.Tk()
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
    global level_one_image
    global ninja_image
    ninja_image_file = Image.open("./assets/ninja.png")
    ninja_image = ImageTk.PhotoImage(ninja_image_file.resize((30, 30)))
    level_one_image_file = Image.open("./assets/forest_level_background.jpeg")
    level_one_image = ImageTk.PhotoImage(level_one_image_file.resize((2000, 2000)))

    # Game data widgets
    character = tk.Label(canvas, image=ninja_image, background="white")
    character.grid(row=user_interface_data["character"][1], column=user_interface_data["character"][0])

    # Add background image to canvas
    canvas.create_image(0, 0, image=level_one_image)

    # root.mainloop()


# user_interface(number_of_rows, number_of_columns, user_interface_data)


def main():
    pass


if __name__ == "__main__":
    main()
