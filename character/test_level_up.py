"""
ADD DOCSTRING
"""
from unittest import TestCase
from level_up import level_up


class Test(TestCase):

    def test_level_up_input_attack_full_word(self):
        character_attack = {"Attack Level": 0, "Max HP": 50, "Current HP": 45}
        level_up(character_attack, "attack")
        expected_character = {'Attack Level': 1, 'Max HP': 50, 'Current HP': 45}
        self.assertEqual(expected_character, character_attack)

    def test_level_up_input_defense_full_word(self):
        character_defense = {"Attack Level": 0, "Max HP": 50, "Current HP": 45}
        level_up(character_defense, "defense")
        expected_character = {'Attack Level': 0, 'Max HP': 60, 'Current HP': 45}
        self.assertEqual(expected_character, character_defense)

    def test_level_up_input_defense_single_letter(self):
        character_defense = {"Attack Level": 0, "Max HP": 50, "Current HP": 45}
        level_up(character_defense, "d")
        expected_character = {'Attack Level': 0, 'Max HP': 60, 'Current HP': 45}
        self.assertEqual(expected_character, character_defense)

    def test_level_up_input_attack_single_letter(self):
        character_attack = {"Attack Level": 0, "Max HP": 50, "Current HP": 45}
        level_up(character_attack, "a")
        expected_character = {'Attack Level': 1, 'Max HP': 50, 'Current HP': 45}
        self.assertEqual(expected_character, character_attack)

    def test_level_up_input_attack_number_input(self):
        character_attack = {"Attack Level": 0, "Max HP": 50, "Current HP": 45}
        level_up(character_attack, "1")
        expected_character = {'Attack Level': 1, 'Max HP': 50, 'Current HP': 45}
        self.assertEqual(expected_character, character_attack)

    def test_level_up_input_defense_number_input(self):
        character_defense = {"Attack Level": 0, "Max HP": 50, "Current HP": 45}
        level_up(character_defense, "2")
        expected_character = {'Attack Level': 0, 'Max HP': 60, 'Current HP': 45}
        self.assertEqual(expected_character, character_defense)

    def test_level_up_input_invalid_input(self):
        character_defense = {"Attack Level": 0, "Max HP": 50, "Current HP": 45}
        level_up(character_defense, "p")
        expected_character = {'Attack Level': 0, 'Max HP': 50, 'Current HP': 45}
        self.assertEqual(expected_character, character_defense)

    def test_level_up_input_invalid_input_boolean(self):
        character_defense = {"Attack Level": 0, "Max HP": 50, "Current HP": 45}
        actual = level_up(character_defense, "p")
        expected = False
        self.assertEqual(expected, actual)

    def test_level_up_input_valid_input_boolean(self):
        character_defense = {"Attack Level": 0, "Max HP": 50, "Current HP": 45}
        actual = level_up(character_defense, "a")
        expected = True
        self.assertEqual(expected, actual)

