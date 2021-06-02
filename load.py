from runes import Runes
from utils import auto_str
from pet import Pet


@auto_str
class Bonus:
    def __init__(self, **kwargs):
        pass


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
