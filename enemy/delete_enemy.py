"""
Tommy Ju
A01347715
"""


def delete_enemy(enemies, enemy_widgets, vision_cones, vision_cone_widgets, enemy_index):
    # remove enemy completely after successful fight
    enemy_widgets[enemy_index].destroy()
    enemy_widgets.pop(enemy_index)
    enemies.pop(enemy_index)
    vision_cone_widgets[enemy_index].destroy()
    vision_cone_widgets.pop(enemy_index)
    vision_cones.pop(enemy_index)


def main():
    pass


if __name__ == "__main__":
    main()
