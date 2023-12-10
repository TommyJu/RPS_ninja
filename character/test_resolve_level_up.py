"""
ADD DOCSTRING
"""
from unittest import TestCase
from level_up import resolve_level_up


class Test(TestCase):
    def test_resolve_level_up_attack(self):
        character_attack = {"Attack Level": 0, "Max HP": 50, "Current HP": 45}
        actual = resolve_level_up("attack", character_attack)
        expected_character = {'Attack Level': 1, 'Max HP': 50, 'Current HP': 45}
        self.assertEqual(expected_character, actual)

    def test_resolve_level_up_defense(self):
        character_attack = {"Attack Level": 0, "Max HP": 50, "Current HP": 45}
        actual = resolve_level_up("defense", character_attack)
        expected_character = {'Attack Level': 0, 'Max HP': 60, 'Current HP': 45}
        self.assertEqual(expected_character, actual)
