"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""
import random


def make_vision_cone(enemy_coordinates):
    """

    :param enemy_coordinates:
    :return:
    """
    vision_cones = []
    for enemy in enemy_coordinates:
        direction = random.choice(["north", "east", "south", "west"])
        match direction:
            case"north":
                vision_cones.append([enemy[0], enemy[1] - 1])
            case "east":
                vision_cones.append([enemy[0] + 1, enemy[1]])
            case "south":
                vision_cones.append([enemy[0], enemy[1] + 1])
            case "west":
                vision_cones.append([enemy[0] - 1, enemy[1]])
    return vision_cones


def main():
    pass


if __name__ == "__main__":
    main()
