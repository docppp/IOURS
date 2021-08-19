from .loader_base import LoaderBase, Singleton
from .loader_pets import LoaderPets
from .loader_ship import LoaderShip
from .loader_spinbox import LoaderSpinbox


class LoaderMaster(metaclass=Singleton):

    def __init__(self):
        self.pets = LoaderPets()
        self.spinbox = LoaderSpinbox()
        self.ship = LoaderShip()

    def re(self):
        self.pets.reload()
        self.spinbox.reload()
        self.ship.reload()

    @staticmethod
    def loadFile(file="iou.txt"):
        base = LoaderBase()
        base.loadFile(file)

