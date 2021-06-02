import unittest
from unittest import mock
from .test_coverage import TestCoverage
from .test_mock_content import mock_content
from ldr.loader_base import LoaderBase


class TestLoaderBase(unittest.TestCase, TestCoverage):
    test_class = LoaderBase

    @classmethod
    def setUpClass(cls):
        cls.loader = LoaderBase()
        mocked_open_function = mock.mock_open(read_data=mock_content)
        with mock.patch("builtins.open", mocked_open_function):
            cls.loader.loadFile()

    def test_loadFile(self):
        check = [line+"\n" for line in mock_content.split("\n") if line]
        self.assertEqual(check, self.loader.file_content)

    def test_reload(self):
        # Loader Base does not reload things
        pass


if __name__ == '__main__':
    unittest.main()
