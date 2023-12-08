"""
Tommy Ju
A01347715
"""


# Delete all enemies
for enemy_widget, vision_cone_widget in zip(enemy_widgets, vision_cone_widgets):
    enemy_widget.destroy()
    vision_cone_widget.destroy()
    # Generate new enemies
    enemies = make_enemy(board)
    # Reset character position
    character["X-coordinate"] = 0
    character["Y-coordinate"] = 0


def main():
    pass


if __name__ == "__main__":
    main()
