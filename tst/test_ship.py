import unittest
from unittest import mock
from .test_coverage import TestCoverage
from .test_mock_content import mock_content
from ldr.loader_ship import LoaderShip
from ldr.loader_spinbox import LoaderSpinbox
from sas.bonus import BonusChar
from sas.ship import Ship


class TestShip(unittest.TestCase, TestCoverage):
    test_class = Ship

    @classmethod
    def setUpClass(cls):
        cls.loader = LoaderShip()
        mocked_open_function = mock.mock_open(read_data=mock_content)
        with mock.patch("builtins.open", mocked_open_function):
            cls.loader.loadFile()
        cls.spinbox = LoaderSpinbox().getSpinbox()
        cls.bonus_guild = cls.loader.getBonusGuild()
        cls.bonus_char = BonusChar().loadSpinbox(cls.spinbox)
        cls.ship = Ship()
        cls.ship.lvl_weapon = 115
        cls.ship.lvl_reactor = 2
        cls.ship.lvl_hull = 118
        cls.ship.lvl_wings = 125

    def test_createShipDict(self):
        ship_dict = self.ship.createShipDict(3, self.bonus_guild, self.bonus_char)
        comparison = {
            'speed': 247.5,
            'armor': 20.0,
            'hp': 227171.39803776,
            'dmg': 89981.69831928643,
            'armor_pen': 1.425,
            'regen_hp': 12494.426892076799,
            'leech': 0.415,
            'absorb': 0.04,
            'reflection': 0.28,
            'number': 3}
        self.assertEqual(ship_dict, comparison)

    def test_calculateCost(self):
        ult, imat = self.ship.calculateCost()
        self.assertEqual(1791835, ult)
        self.assertEqual(1899680, imat)



