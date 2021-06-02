import unittest
from .test_loader_base import TestLoaderBase
from .test_loader_pets import TestLoaderPets
from .test_loader_spinbox import TestLoaderSpinbox
from .test_opponent import TestOpponent
from .test_pet import TestPet
from .test_runes import TestRunes

if __name__ == '__main__':
    # Create tests class, so imports are not unused.
    TestLoaderBase()
    TestLoaderPets()
    TestLoaderSpinbox()
    TestOpponent()
    TestPet()
    TestRunes()
    unittest.main()
