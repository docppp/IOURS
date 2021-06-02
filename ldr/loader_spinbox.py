from .loader_base import LoaderBase, Singleton


class LoaderSpinbox(LoaderBase, metaclass=Singleton):

    def __init__(self):
        super().__init__()
        self.spinbox = {}
        self.getters = ['getSpinbox']
        self._raw_lines = {
            'rune_1_rarity': 18,
            'rune_1_level': 19,
            'rune_2_rarity': 20,
            'rune_2_level': 21,
            'op_level': 22,
        }

    def getSpinbox(self):
        self.spinbox = {}
        for key in self._raw_lines:
            self.spinbox[key] = self._getRawLine(key)[0].strip()
        return self.spinbox
