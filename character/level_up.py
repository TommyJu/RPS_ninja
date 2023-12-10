"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""


def level_up(character: dict, user_input: str) -> dict:
    """
    Alter the user dictionary to reflect there chosen upgrade

    :param character: dictionary representing the player character
    :param user_input: string obtained from the GUI
    :precondition: character must be a dictionary with keys "Attack Level", "Max HP" with values being integers
    :return: dictionary with changes that reflect user choice
    """
    acceptable_inputs = {"attack", "defense",
                         "a", "d",
                         "1", "2"}
    equivalent_inputs = [["attack", "a", "1"],
                         ["defense", "d", "2"]]

    print("You have completed a great feat\n"
          "by doing so you have leveled up\n\n"
          "Choose between \n"
          "1.(D)efense\n"
          "2.(A)ttack\n")
    user_input = user_input.strip()
    for choices in equivalent_inputs:
        if user_input.lower() in choices:
            return resolve_level_up(choices[0], character)


def resolve_level_up(user_choice: str, character: dict) -> dict:
    """
    Change dictionary based on string inputted

    :param user_choice: string
    :param character: dictionary
    :precondition: Player is currently leveling up "defense"
                   user_choice must be a string of either "attack" or "defense"
                   character must be a dictionary of
    :postcondition: correctly alters dictionary value for the correct key
    :return: dictionary that is altered
    >>> character_attack = {"Attack Level": 0, "Max HP": 50, "Current HP": 45}
    >>> resolve_level_up("attack", character_attack)
    {'Attack Level': 1, 'Max HP': 50, 'Current HP': 45}

    >>> character_defense = {"Attack Level": 0, "Max HP": 50, "Current HP": 45}
    >>> resolve_level_up("defense", character_defense)
    {'Attack Level': 0, 'Max HP': 60, 'Current HP': 45}
    """
    match user_choice:
        case "attack":
            character["Attack Level"] += 1
            return character
        case "defense":
            character["Max HP"] += 10
            return character


def main():
    pass


if __name__ == "__main__":
    main()
