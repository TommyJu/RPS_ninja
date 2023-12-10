"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""


def resolve_quick_time(quick_time_result: tuple, character: dict):
    """
    change character dictionary value according to the results of the quick time event

    :param quick_time_result: tuple containg a Boolean value and a string
    :param character: dicitonary representing player character
    :precondition: quick_time_result must be a tuple where index 0 is a Boolean value and index 1 is a string
                   the string in quick time event must be one of "no damage", "minimal damage", "significant damage"
                   character must be a dictionary with key "Current HP" and "Attack Level" both with integer values
                   Character key-value "Current HP" must be greater than 0
    :postcondition: character dictionary values will change according to quick_time_result
                    if the boolean value in quick_time_event determines if "Current HP" will decrease
                    the string in quick_time_event will determine the change in "Attack Level"
    :return: dictionary that is changed according to results
    """
    if not quick_time_result[0]:
        match quick_time_result[1]:
            case "no damage":
                return character
            case "minimal damage":
                character["Attack Level"] -= 1
                return character
            case "significant damage":
                character["Attack Level"] -= 3
                return character
    else:
        if quick_time_result[1] == "counter":
            character["Current HP"] += 1
            character["Attack Level"] += 1
            return character
        return character

def main():
    pass


if __name__ == "__main__":
    main()
