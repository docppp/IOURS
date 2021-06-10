import unittest
from tst.test_loader_base import TestLoaderBase
from tst.test_loader_pets import TestLoaderPets
from tst.test_loader_spinbox import TestLoaderSpinbox
from tst.test_opponent import TestOpponent
from tst.test_pet import TestPet
from tst.test_runes import TestRunes

if __name__ == '__main__':
    # Create tests class, so imports are not unused.
    TestLoaderBase()
    TestLoaderPets()
    TestLoaderSpinbox()
    TestOpponent()
    TestPet()
    TestRunes()
    unittest.main()
