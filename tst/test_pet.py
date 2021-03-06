import unittest
from unittest import mock
from .test_coverage import TestCoverage
from .test_mock_content import mock_content
from ldr.loader_pets import LoaderPets
from rns.opponent import Opponent
from rns.pet import Pet


class TestPet(unittest.TestCase, TestCoverage):
    test_class = Pet

    @classmethod
    def setUpClass(cls):
        cls.loader = LoaderPets()
        mocked_open_function = mock.mock_open(read_data=mock_content)
        with mock.patch("builtins.open", mocked_open_function):
            cls.loader.loadFile()

    def test_prepareForFight(self):
        pet1, pet2 = self.loader.getPets()
        bonus = self.loader.getBonus()
        runes = self.loader.getRunes()
        op = Opponent.generateOpponent(600, bonus.armor, runes.frenzy)
        pet = pet1.prepareForFight(op, bonus, runes)
        self.assertEqual(pet.dmg, 46368113205)
        self.assertEqual(pet.hp, 612245)
        self.assertEqual(pet.regen, 122448)
        self.assertEqual(pet.reduced_regen, 122448)
        self.assertEqual(pet.heal, 551020)
