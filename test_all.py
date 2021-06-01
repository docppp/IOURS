import unittest
from test_loader_base import TestLoaderBase
from test_loader_pets import TestLoaderPets
from test_loader_spinbox import TestLoaderSpinbox

if __name__ == '__main__':
    TestLoaderBase()
    TestLoaderPets()
    TestLoaderSpinbox()
    unittest.main()
