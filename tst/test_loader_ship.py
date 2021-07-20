import unittest
from unittest import mock
from .test_coverage import TestCoverage
from .test_mock_content import mock_content
from ldr.loader_ship import LoaderShip


class TestLoaderShip(unittest.TestCase, TestCoverage):
    test_class = LoaderShip

    @classmethod
    def setUpClass(cls):
        cls.loader = LoaderShip()
        mocked_open_function = mock.mock_open(read_data=mock_content)
        with mock.patch("builtins.open", mocked_open_function):
            cls.loader.loadFile()

    def test_getBonusGuild(self):
        bonus = self.loader.getBonusGuild()
        self.assertAlmostEqual(bonus.space_academy, 6.7985)
        self.assertAlmostEqual(bonus.guild_passive, 1.1480)


if __name__ == '__main__':
    unittest.main()
