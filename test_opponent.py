import unittest
from unittest import mock
from test_coverage import TestCoverage
from opponent import Opponent
from loader_pets import LoaderPets
from test_mock_content import mock_content


class TestOpponent(unittest.TestCase, TestCoverage):
    test_class = Opponent

    @classmethod
    def setUpClass(cls):
        cls.loader = LoaderPets()
        mocked_open_function = mock.mock_open(read_data=mock_content)
        with mock.patch("builtins.open", mocked_open_function):
            cls.loader.loadFile()

    def test_generateOpponent(self):
        bonus = self.loader.getBonus()
        runes = self.loader.getRunes()
        op = Opponent.generateOpponent(600, bonus.armor, runes.frenzy)
        self.assertEqual(op.dmg, 9036341)
        self.assertEqual(op.hp, 70205536902626)
        self.assertEqual(op.base_dmg, 401615137)
        self.assertEqual(op.shield, 165)
        self.assertEqual(op.defense, 15.5)
