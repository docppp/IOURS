from .loader_base import LoaderBase, Singleton


class LoaderSpinbox(LoaderBase, metaclass=Singleton):

    def __init__(self):
        super().__init__()
        self.spinbox = {}
        self.getters = ['getSpinbox']
        self._raw_lines = {
            # pets related
            'rune_1_rarity': 18,
            'rune_1_level': 19,
            'rune_2_rarity': 20,
            'rune_2_level': 21,
            'op_level': 22,
            # ship related
            'virtue': 25,
            'orb_star': 26,
            'orb_level': 27,
            'legendary': 28,
            'asc_dmg': 29,
            'asc_hp': 30,
            'trophy_hp': 31,
            'trophy_dmg': 32,
        }

    def getSpinbox(self):
        self.spinbox = {}
        for key in self._raw_lines:
            self.spinbox[key] = self._getRawLine(key)[0].strip()
        return self.spinbox
