import unittest
from test_coverage import TestCoverage
from runes import Runes


class TestRunes(unittest.TestCase, TestCoverage):
    test_class = Runes

    def test_createRunes(self):
        rune1 = Runes.createRunes(30, 0, 0.1, 'adrenaline', 'anger', 'favor', 'frenzy')
        self.assertAlmostEqual(rune1.arena, 0.1)
        self.assertAlmostEqual(rune1.adrenaline, 1.628)
        self.assertAlmostEqual(rune1.anger, 0.2035)
        self.assertAlmostEqual(rune1.favor, 0.0814)
        self.assertAlmostEqual(rune1.frenzy, 0.407)
        self.assertAlmostEqual(rune1.poison, 0)
        self.assertAlmostEqual(rune1.regen, 0)

        rune2 = Runes.createRunes(18, 4, 0.1, 'poison', 'regen', 'poison')
        self.assertAlmostEqual(rune2.arena, 0.1)
        self.assertAlmostEqual(rune2.adrenaline, 0)
        self.assertAlmostEqual(rune2.anger, 0)
        self.assertAlmostEqual(rune2.favor, 0)
        self.assertAlmostEqual(rune2.frenzy, 0)
        self.assertAlmostEqual(rune2.poison, 0.474375)
        self.assertAlmostEqual(rune2.regen, 0.253)

        rune3 = Runes.createRunes(31, 1, 0.1, 'adrenaline', 'adrenaline', 'adrenaline', 'favor')
        self.assertAlmostEqual(rune3.arena, 0.1)
        self.assertAlmostEqual(rune3.adrenaline, 2.9491)
        self.assertAlmostEqual(rune3.anger, 0)
        self.assertAlmostEqual(rune3.favor, 0.08426)
        self.assertAlmostEqual(rune3.frenzy, 0)
        self.assertAlmostEqual(rune3.poison, 0)
        self.assertAlmostEqual(rune3.regen, 0)

    def test_runesCombList(self):
        comb1, comb2 = Runes.runesCombList(30, 0, 15, 0, 0)
        self.assertEqual(len(comb1), 1296)
        self.assertEqual(len(comb2), 216)
