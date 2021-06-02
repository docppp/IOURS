from .loader_base import LoaderBase, Singleton
from .loader_pets import LoaderPets
from .loader_spinbox import LoaderSpinbox


class LoaderMaster(LoaderBase, metaclass=Singleton):

    def __init__(self, file="iou.txt"):
        super().__init__(file)
        self.pets = LoaderPets(file)
        # self.spinbox = LoaderSpinbox()
        print("Master created", id(self), "pets:", id(self.pets))


    def reload(self):
        print("I am Master", id(self), "called reload")
        self.pets.reload()
        # self.spinbox.reload()

