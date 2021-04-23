from copy import copy
from math import floor
from fight import fight
from runes import runesCombList
from utils import auto_str


@auto_str
class Opponent:
    def __init__(self, **kwargs):
        pass


def generateOpponent(level, bonus_armor, runes_frenzy):
    op = Opponent()
    op.level = level
    bonus_diff = max(0, (op.level - 5) * 5) + max(0, (op.level - 10) * 2) + max(0, (op.level - 20) * 10)
    diff_mod = 5 + op.level * 5 + bonus_diff + op.level ** 2 / 5
    level_mod = floor(min(op.level, 30) / 5)
    mod5 = max(0, floor((op.level - 35) / 5))
    hp_mod = (1 + (max(0, op.level - 100)) ** 1.5 * 0.01) * (1.1 ** floor(op.level * 0.01) if op.level > 100 else 1)
    dmg_mod = (1 + (max(0, op.level - 100)) ** 1.5 * 0.01) * (1.1 ** floor(op.level * 0.003) if op.level > 100 else 1)
    op.hp = round(diff_mod * (op.level + 1) ** 2 * (
            min(1, 0.15 + 0.1 * level_mod) + (max(0, op.level - 35) + mod5) / 50) * hp_mod * 0.8)
    op.defense = 1 + max(0, op.level - 250) * 0.01 + (1 + (op.level - 500) * 0.1 if op.level > 500 else 0)
    op.shield = int(floor(max(0, op.level - 450) * 0.1) * (1 + max(0, op.level - 500) * 0.1))
    op.base_dmg = int((5 + (op.level + 1) ** 1.6 *
                       (0.15 + (0.085 * level_mod) + max(0, op.level - 35) * 0.1 + mod5 * 0.08) *
                       dmg_mod) * 2.5 * (1 + runes_frenzy*0.1) * 0.70)
    op.dmg = round(op.base_dmg * bonus_armor / 2)
    return op


def preparePet(pet, opponent, bonus, runes):
    ret_pet = copy(pet)
    ret_pet.dmg = int(pet.dmg/opponent.defense*(1+runes.frenzy)/(1+runes.adrenaline*0.1))
    ret_pet.regen = int(pet.hp*(bonus.regen+runes.regen))
    ret_pet.heal = int(pet.hp*bonus.heals)
    return ret_pet


def calculateHeals(pet1, pet2, bonus, runes, level):
    op = generateOpponent(level, bonus.armor, runes.frenzy)
    p1 = preparePet(pet1, op, bonus, runes)
    p2 = preparePet(pet2, op, bonus, runes)
    return fight(p1, p2, bonus, runes, op)


def getBestRunes(pet1, pet2, bonus, rune1_rarity, rune1_level, rune2_rarity, rune2_level, opponent_level):
    min_heals = 99999999
    rcopy1 = 'er'
    rcopy2 = 'er'
    list_rune1, list_rune2 = runesCombList(rune1_rarity, rune1_level, rune2_rarity, rune2_level)
    for rune1 in list_rune1:
        for rune2 in list_rune2:
            rune = rune1 + rune2
            cur_heals = calculateHeals(pet1, pet2, bonus, rune, opponent_level)
            if cur_heals < min_heals:
                min_heals = cur_heals
                rcopy1 = copy(rune1)
                rcopy2 = copy(rune2)
    print(min_heals)
    print(rcopy1.__repr__())
    print(rcopy2.__repr__())
    return rcopy1, rcopy2, min_heals
