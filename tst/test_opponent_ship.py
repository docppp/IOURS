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
