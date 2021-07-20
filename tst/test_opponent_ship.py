import unittest
from .test_coverage import TestCoverage
from sas.opponent import Opponent


class TestOpponentShip(unittest.TestCase, TestCoverage):
    test_class = Opponent

    def test_generateOpponent(self):
        op = Opponent.generateOpponent(70)
        self.assertAlmostEqual(op.level, 70)
        self.assertAlmostEqual(op.health, 2376.0)
        self.assertAlmostEqual(op.shield, 1138.5)
        self.assertAlmostEqual(op.eff_shield, 2732.4)
        self.assertAlmostEqual(op.dmg, 301.125)
        self.assertAlmostEqual(op.speed, 107.58)

        op = Opponent.generateOpponent(570)
        self.assertAlmostEqual(op.level, 570)
        self.assertAlmostEqual(op.health, 85386)
        self.assertAlmostEqual(op.shield, 42493.5)
        self.assertAlmostEqual(op.eff_shield, 526919.4)
        self.assertAlmostEqual(op.dmg, 10689.875)
        self.assertAlmostEqual(op.speed, 3465.98)

    def test_createShipDict(self):
        ship_dict = Opponent.generateOpponent(800).createShipDict()
        comparison = {
            'speed': 7958.34,
            'armor': 98360.49999999999,
            'hp': 197257.99999999997,
            'dmg': 24679.624999999996,
            'armor_pen': 1,
            'regen_hp': 0,
            'leech': 0,
            'absorb': 15.98,
            'reflection': 0,
            'number': 4}
        self.assertEqual(ship_dict, comparison)
