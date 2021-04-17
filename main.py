from load import loadThings
from utils import generateOpponent, preparePet
from fight import fight
from runes import runesGenerator, runesCombList
from copy import copy

pet1, pet2, bonus, runes = loadThings()


def calculateHeals(pet1, pet2, bonus, runes, level):
    op = generateOpponent(level, bonus.armor, runes.frenzy)
    p1 = preparePet(pet1, op, bonus, runes)
    p2 = preparePet(pet2, op, bonus, runes)
    return fight(p1, p2, bonus, runes, op)


def getBestRunes(rune1_rarity, rune1_level, rune2_rarity, rune2_level, opponent_level):
    min_heals = 99999999
    rcopy1 = ''
    rcopy2 = ''
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
    print(rcopy1)
    print(rcopy2)
    return rcopy1, rcopy2, min_heals


# TODO
# fight function in C would be speed boost
# but I have no idea how to import it correctly
# path = str(os.path.join(pathlib.Path(), "fight.dll"))
# from ctypes import CDLL
# c_lib = CDLL("fight")
# func0 = c_lib.fight
# func0.restype = c_int
# res = func0()
# print("{0:s} returned {1:d}".format(func0.__name__, res))
#
# ans = c_lib.fight(3132840264, 73837, 26285, 28796,
#                   3132840264, 73837, 26285, 28796,
#                   c_float(9.92), c_float(0.84),
#                   c_float(0.0975), c_float(0), c_float(0.074),
#                   351555789279, 0, 344983)
# print(ans)
