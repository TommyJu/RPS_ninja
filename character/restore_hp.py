"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""


def restore_hp(character: dict) -> dict:
    """
    Changes dictionary value of key "Current HP" to equal "Max HP" value

    :param character: dictionary representing an entity with HP
    :precondition: character must be a dictionary with keys "Current HP" and "Max HP" with both values being an integer
                   "Current HP" must be less equal to or less than "Max HP"
    :postcondition: correctly alters the dictionary character
    :return: dictionary that has been changed

    >>> restore_hp({"Current HP":1, "Max HP":50})
    {'Current HP': 50, 'Max HP': 50}

    >>> restore_hp({'Current HP': 60, 'Max HP':60})
    {'Current HP': 60, 'Max HP': 60}
    """
    character["Current HP"] = character["Max HP"]
    return character

def main():
    pass


if __name__ == "__main__":
    main()
