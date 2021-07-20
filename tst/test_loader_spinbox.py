import unittest
from unittest import mock
from .test_coverage import TestCoverage
from .test_mock_content import mock_content
from ldr.loader_spinbox import LoaderSpinbox


class TestLoaderSpinbox(unittest.TestCase, TestCoverage):
    test_class = LoaderSpinbox

    @classmethod
    def setUpClass(cls):
        cls.loader = LoaderSpinbox()
        mocked_open_function = mock.mock_open(read_data=mock_content)
        with mock.patch("builtins.open", mocked_open_function):
            cls.loader.loadFile()

    def test_getSpinbox(self):
        spinbox = self.loader.getSpinbox()
        checked = {
            'rune_1_rarity': '20',
            'rune_1_level': '0',
            'rune_2_rarity': '19',
            'rune_2_level': '1',
            'op_level': '600',
            'virtue': '72',
            'orb_star': '7',
            'orb_level': '0',
            'legendary': '50',
            'asc_dmg': '10',
            'asc_hp': '10',
            'trophy_hp': '100',
            'trophy_dmg': '100',
        }
        self.assertEqual(spinbox, checked)
