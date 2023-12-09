"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""


def get_choice_combat(attack_input):
    """
    prompt user to choose how they want to attack

    :param attack_input: a string from the GUI input
    :precondition: valid input is entered
    :postcondtion: retrieves the desired attack choice for valid input
                   print input prompt if valid input is not given
    :return: string representing rock, paper, or scissor, or None if invalid
    """
    valid_input = ['1', '2', '3', 'rock', 'paper', 'scissor', 'r', 'p', 's']
    equivalent_inputs = [["rock", "r", "1"],
                         ["paper", "p", "2"],
                         ["scissor", "s", "3"]]
    print("Choose your weapon to defeat the enemy\n"
          "1. (R)ock\n"
          "2. (P)aper\n"
          "3. (S)cissor\n")
    attack_input = attack_input.strip()
    if attack_input.lower() in valid_input:
        for attack_choice in equivalent_inputs:
            if attack_input.lower() in attack_choice:
                return attack_choice[0]
    else:
        return None


def main():
    pass


if __name__ == "__main__":
    main()
