import unittest
from unittest import mock
from unittest.mock import patch
from test_coverage import TestCoverage
from load import Loader

mock_content = """AP Arena Stats	
Pet 1	Pet 2
1,000,000,000,001	1,000,000,000,002
3,000,001	3,000,002
4.50%	Heals
3000.00%	90.00%
30.00%	Favor
1.0%	70.0000%
2.0%	
Arena	66.675%
Adrenaline Rush	390.0000%
Anger Issues	4.0%
Favor	70.0000%
Frenzy	0.1%
Poisonous	0.2%
Premeditated	0.3%
Regen	10%
Converge 100%
20
0
20
0
690
"""


class TestLoader(unittest.TestCase, TestCoverage):
    test_class = Loader

    @classmethod
    def setUpClass(cls):
        cls.loader = Loader()
        mocked_open_function = mock.mock_open(read_data=mock_content)
        with mock.patch("builtins.open", mocked_open_function):
            cls.loader.loadFile()

    def test_loadFile(self):
        check = [line+"\n" for line in mock_content.split("\n") if line]
        self.assertEqual(check, self.loader.file_content)

    def test_reload(self):
        with patch.object(Loader, 'getBonus') as mock_bonus, \
                patch.object(Loader, 'getRunes') as mock_runes, \
                patch.object(Loader, 'getPets') as mock_pets:
            self.loader.reload()
        mock_bonus.assert_called_once()
        mock_runes.assert_called_once()
        mock_pets.assert_called_once()

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
