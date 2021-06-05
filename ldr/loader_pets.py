from .loader_base import LoaderBase, Singleton
from rns.bonus import Bonus
from rns.pet import Pet
from rns.runes import Runes


class LoaderPets(LoaderBase, metaclass=Singleton):

    def __init__(self):
        super().__init__()
        self.bonus = None
        self.runes = None
        self.pets = None
        self.getters = ['getBonus', 'getRunes', 'getPets']
        self._raw_lines = {
            'raw_dmg': 2,
            'raw_hp': 3,
            'raw_armor': 4,
            'raw_reflect_heals': 5,
            'raw_regen': 6,
            'raw_rune_arena': 9,
            'raw_rune_adrenaline': 10,
            'raw_rune_frenzy': 13,
            'raw_rune_regen': 16,
            'raw_converge': 17,
        }

    def getBonus(self):
        raw_armor, text = self._getRawLine('raw_armor')
        raw_reflect, raw_heals = self._getRawLine('raw_reflect_heals')
        raw_regen, text = self._getRawLine('raw_regen')
        text, raw_rune_regen = self._getRawLine('raw_rune_regen')
        text, raw_converge = self._getRawLine('raw_converge', ' ')
        self.bonus = Bonus()
        self.bonus.armor = float(raw_armor[:-1]) / 100
        self.bonus.reflect = float(raw_reflect[:-1]) / 100
        self.bonus.heals = float(raw_heals[:-2]) / 100
        self.bonus.regen = (float(raw_regen[:-1]) / 100) - (float(raw_rune_regen[:-2]) / 100)
        self.bonus.converge = float(raw_converge[:-2]) / 100
        return self.bonus

    def getRunes(self):
        text, raw_rune_arena = self._getRawLine('raw_rune_arena')
        self.runes = Runes()
        self.runes.arena = float(raw_rune_arena[:-2]) / 100
        return self.runes

    def getPets(self):
        raw_dmg1, raw_dmg2 = self._getRawLine('raw_dmg')
        raw_hp1, raw_hp2 = self._getRawLine('raw_hp')
        text, raw_rune_adrenaline = self._getRawLine('raw_rune_adrenaline')
        text, raw_rune_frenzy = self._getRawLine('raw_rune_frenzy')
        adrenaline = float(raw_rune_adrenaline[:-2]) / 100
        frenzy = float(raw_rune_frenzy[:-2]) / 100
        pet1 = Pet()
        pet2 = Pet()
        pet1.dmg = float(int(raw_dmg1.replace(',', '')) / ((1 + frenzy) * (1 + adrenaline * 0.1)))
        pet2.dmg = float(int(raw_dmg2.replace(',', '')) / ((1 + frenzy) * (1 + adrenaline * 0.1)))
        pet1.hp = float(int(raw_hp1.replace(',', '')) / (1 + adrenaline))
        pet2.hp = float(int(raw_hp2.replace(',', '')) / (1 + adrenaline))
        self.pets = pet1, pet2
        return self.pets
