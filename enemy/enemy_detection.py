"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""
from combat.engage_combat import engage_combat


def enemy_detection(character, enemies, vision_cones):
    """
    Check if character coordinates overlaps with an enemy or their vision cone

    :param character: dictionary representing the user's character
    :param enemies: list of lists representing coordinates of enemies
    :param vision_cones: list of lists or none representing coordinates of vision cones
    :precondition: character is a dictionary with key "Current HP" with values being integer
                   character "Current HP" value is greater than 0 at beginning of engage combat
                   enemy_coordinates list of list representing the enemy current location
                   vision_cones list of lists representing the enemy detection or none if enemy is looking at location
                   not on board
    :postcondition: determines if character overlaps with a coordinate on either the enemies or vision cones list
                    if overlap occurs, index of enemy is found and initiates engage_combat function with index found
                    if no overlap no change occurs
    """
    character_coordinate = [character["X-coordinate"], character["Y-coordinate"]]
    if character_coordinate in enemies:
        enemy_index = enemies.index(character_coordinate)
        engage_combat(character, enemies, vision_cones, enemy_index)
        tuple_true = (True, enemy_index)
        return tuple_true
    elif character_coordinate in vision_cones:
        enemy_index = vision_cones.index(character_coordinate)
        engage_combat(character, enemies, vision_cones, enemy_index)
        tuple_true = (True, enemy_index)
        return tuple_true
    else:
        return False


def main():
    pass


if __name__ == "__main__":
    main()
