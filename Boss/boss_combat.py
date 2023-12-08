"""
Tommy Ju
A01347715
Matthew Yoon
A01373290
"""
import random

from is_boss_alive import is_boss_alive
from quick_time_event import quick_time_event
from choose_boss_attack_pattern import choose_boss_attack_pattern
from make_boss import make_boss
from character.is_alive import is_alive
from combat.does_player_win import does_player_win
from combat.get_choice_combat import get_choice_combat


def boss_combat(character, boss):
    while is_boss_alive(boss) and is_alive(character):
        enemy_action = (choose_boss_attack_pattern(), random.randint(2, 12))
        player_action = (get_choice_combat(), random.randint(0,10) + character["Attack Level"])
        does_player_win(player_action, enemy_action)



def main():
    pass


if __name__ == "__main__":
    main()
