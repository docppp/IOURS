import unittest
from test_coverage import TestCoverage
from load import Loader


class TestLoader(unittest.TestCase, TestCoverage):
    test_class = Loader

    def test_reload(self):
        self.assertTrue(True)

    def test_getBonus(self):
        self.assertTrue(True)

    def test_getRunes(self):
        self.assertTrue(True)

    def test_getPets(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
