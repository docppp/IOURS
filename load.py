from utils import auto_str


@auto_str
class Pet:
    def __init__(self, **kwargs):
        pass


@auto_str
class Bonus:
    def __init__(self, **kwargs):
        pass


@auto_str
class Runes:
    def __init__(self, **kwargs):
        self.first = 'none'
        self.second = 'none'
        self.third = 'none'
        self.fourth = 'none'

    def __add__(self, other):
        r = Runes()
        r.adrenaline = self.adrenaline + other.adrenaline
        r.anger = self.anger + other.anger
        r.favor = self.favor + other.favor
        r.frenzy = self.frenzy + other.frenzy
        r.poison = self.poison + other.poison
        r.regen = self.regen + other.regen
        return r

    def __repr__(self):
        if self.fourth == 'none' and self.third == 'none':
            return f'{self.first}, {self.second}'
        if self.fourth == 'none':
            return f'{self.first}, {self.second}, {self.third}'
        return f'{self.first}, {self.second}, {self.third}, {self.fourth}'


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Loader(metaclass=Singleton):

    _raw_lines = {
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

    def __init__(self, file="iou.txt"):
        self.bonus = None
        self.runes = None
        self.pets = None
        self.file_path = file
        with open(self.file_path) as file:
            self.file_content = file.readlines()
        try:
            self.getBonus()
            self.getRunes()
            self.getPets()
        finally:
            pass

    def reload(self):
        self.getBonus()
        self.getRunes()
        self.getPets()

    def getBonus(self):
        raw_armor, text = self._getRawLine('raw_armor')
        raw_reflect, raw_heals = self._getRawLine('raw_reflect_heals')
        raw_regen, text = self._getRawLine('raw_regen')
        text, raw_rune_regen = self._getRawLine('raw_rune_regen')
        text, raw_converge = self._getRawLine('raw_converge')
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

    def _getRawLine(self, line: str) -> list[str]:
        d = ' ' if line == 'raw_converge' else '\t'
        return self.file_content[self._raw_lines[line]].split(d)


def loadThings() -> (Pet, Pet, Bonus, Runes):
    with open("iou.txt") as file:
        text = file.readline()
        text = file.readline()
        raw_dmg1, raw_dmg2 = file.readline().split('\t')
        raw_hp1, raw_hp2 = file.readline().split('\t')
        raw_armor, text = file.readline().split('\t')
        raw_reflect, raw_heals = file.readline().split('\t')
        raw_regen, text = file.readline().split('\t')
        raw_anger, raw_favor = file.readline().split('\t')
        raw_poison, text = file.readline().split('\t')
        text, raw_rune_arena = file.readline().split('\t')
        text, raw_rune_adrenaline = file.readline().split('\t')
        text, raw_rune_anger = file.readline().split('\t')
        text, raw_rune_favor = file.readline().split('\t')
        text, raw_rune_frenzy = file.readline().split('\t')
        text, raw_rune_poison = file.readline().split('\t')
        text, raw_rune_unused = file.readline().split('\t')
        text, raw_rune_regen = file.readline().split('\t')
        text, raw_converge = file.readline().split(' ')
        spin_r1r = file.readline()
        spin_r1l = file.readline()
        spin_r2r = file.readline()
        spin_r2l = file.readline()
        spin_op = file.readline()

    bonus = Bonus()
    bonus.armor = float(raw_armor[:-1]) / 100
    bonus.reflect = float(raw_reflect[:-1]) / 100
    bonus.heals = float(raw_heals[:-2]) / 100
    bonus.regen = float(raw_regen[:-1]) / 100
    bonus.converge = float(raw_converge[:-2]) / 100

    runes = Runes()
    runes.arena = float(raw_rune_arena[:-2]) / 100
    runes.adrenaline = float(raw_rune_adrenaline[:-2]) / 100
    runes.anger = float(raw_rune_anger[:-2]) / 100
    runes.favor = float(raw_rune_favor[:-2]) / 100
    runes.frenzy = float(raw_rune_frenzy[:-2]) / 100
    runes.poison = float(raw_rune_poison[:-2]) / 100
    runes.regen = float(raw_rune_regen[:-2]) / 100

    pet1 = Pet()
    pet2 = Pet()
    pet1.dmg = float(int(raw_dmg1.replace(',', '')) / ((1 + runes.frenzy) * (1 + runes.adrenaline * 0.1)))
    pet2.dmg = float(int(raw_dmg2.replace(',', '')) / ((1 + runes.frenzy) * (1 + runes.adrenaline * 0.1)))
    pet1.hp = float(int(raw_hp1.replace(',', '')) / (1 + runes.adrenaline))
    pet2.hp = float(int(raw_hp2.replace(',', '')) / (1 + runes.adrenaline))

    bonus.regen -= runes.regen
    runes.adrenaline = 0
    runes.anger = 0
    runes.favor = 0
    runes.frenzy = 0
    runes.poison = 0
    runes.regen = 0

    return pet1, pet2, bonus, runes
