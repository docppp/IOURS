import unittest
from tst.test_loader_base import TestLoaderBase
from tst.test_loader_pets import TestLoaderPets
from tst.test_loader_spinbox import TestLoaderSpinbox
from tst.test_opponent_pet import TestOpponentPet
from tst.test_opponent_ship import TestOpponentShip
from tst.test_pet import TestPet
from tst.test_runes import TestRunes

if __name__ == '__main__':
    # Create tests class, so imports are not unused.
    TestLoaderBase()
    TestLoaderPets()
    TestLoaderSpinbox()
    TestOpponentPet()
    TestOpponentShip()
    TestPet()
    TestRunes()
    unittest.main()
