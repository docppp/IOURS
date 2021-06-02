import unittest
from unittest import mock
from .test_coverage import TestCoverage
from .test_mock_content import mock_content
from ldr.loader_pets import LoaderPets


class TestLoaderPets(unittest.TestCase, TestCoverage):
    test_class = LoaderPets

    @classmethod
    def setUpClass(cls):
        cls.loader = LoaderPets()
        mocked_open_function = mock.mock_open(read_data=mock_content)
        with mock.patch("builtins.open", mocked_open_function):
            cls.loader.loadFile()

    def test_getBonus(self):
        bonus = self.loader.getBonus()
        self.assertEqual(bonus.armor, 0.045)
        self.assertEqual(bonus.reflect, 30)
        self.assertEqual(bonus.heals, 0.9)
        self.assertEqual(bonus.regen, 0.3 - 0.1)
        self.assertEqual(bonus.converge, 1)

    def test_getRunes(self):
        runes = self.loader.getRunes()
        self.assertEqual(runes.arena, 0.66675)
        self.assertEqual(runes.adrenaline, 0)
        self.assertEqual(runes.anger, 0)
        self.assertEqual(runes.favor, 0)
        self.assertEqual(runes.frenzy, 0)
        self.assertEqual(runes.poison, 0)
        self.assertEqual(runes.regen, 0)

    def test_getPets(self):
        pet1, pet2 = self.loader.getPets()
        pet1_dmg = 1000000000001 / ((1 + 0.001) * (1 + 3.90 * 0.1))
        pet2_dmg = 1000000000002 / ((1 + 0.001) * (1 + 3.90 * 0.1))
        pet1_hp = 3000001 / (1 + 3.90)
        pet2_hp = 3000002 / (1 + 3.90)
        self.assertEqual(pet1.dmg, pet1_dmg)
        self.assertEqual(pet2.dmg, pet2_dmg)
        self.assertEqual(pet1.hp, pet1_hp)
        self.assertEqual(pet2.hp, pet2_hp)


if __name__ == '__main__':
    unittest.main()
