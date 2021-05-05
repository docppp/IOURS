from load import Runes
from itertools import product

scaling = {
    "rarity": 12,
    "level": 0.1,
}

efficiency = {
    "adrenaline": 4,
    "anger": 1,
    "favor": 0.8,
    "frenzy": 4,
    "poison": 1.5,
    "regen": 2
}


def getRunesFirstBonus(rarity, level, name):
    return (1 + (rarity * scaling['rarity'] + level) * scaling['level']) / 100 * efficiency[name]


def getRunesSecondBonus(rarity, level, name):
    return (1 + (rarity * scaling['rarity'] + level) * scaling['level']) / 100 * efficiency[name] / 2


def getRunesThirdBonus(rarity, level, name):
    return (1 + (rarity * scaling['rarity'] + level) * scaling['level']) / 100 * efficiency[name] / 4


def getRunesFourthBonus(rarity, level, name):
    return (1 + (rarity * scaling['rarity'] + level) * scaling['level']) / 100 * efficiency[name] / 4


rune_list = ['adrenaline', 'anger', 'favor', 'frenzy', 'poison', 'regen']


def createRunes(rarity, level, first_bonus, second_bonus, third_bonus=None, fourth_bonus=None):
    runes = Runes()
    runes.adrenaline = 0
    runes.anger = 0
    runes.favor = 0
    runes.frenzy = 0
    runes.poison = 0
    runes.regen = 0
    runes.__setattr__(first_bonus, runes.__dict__.get(first_bonus) + getRunesFirstBonus(rarity, level, first_bonus))
    runes.__setattr__(second_bonus, runes.__dict__.get(second_bonus) + getRunesSecondBonus(rarity, level, second_bonus))
    runes.first = first_bonus
    runes.second = second_bonus
    if third_bonus:
        runes.__setattr__(third_bonus, runes.__dict__.get(third_bonus) + getRunesThirdBonus(rarity, level, third_bonus))
        runes.third = third_bonus
    if fourth_bonus:
        runes.__setattr__(fourth_bonus,
                          runes.__dict__.get(fourth_bonus) + getRunesFourthBonus(rarity, level, fourth_bonus))
        runes.fourth = fourth_bonus
    return runes


# TODO:
# Generator seems to be more memory efficient
# but how to stack two generators on top of ech other?
def runesGenerator(rarity, level):
    comb = product(rune_list, rune_list)
    for i in list(comb):
        runes = createRunes(rarity, level, i[0], i[1])
        yield runes


def runesCombList(rarity1, level1, rarity2, level2):
    runes_list1 = []
    runes_list2 = []
    comb1 = runesCombListHelper(rarity1)
    for i in list(comb1):
        runes_list1.append(createRunes(rarity1, level1, i[0], i[1],
                                       i[2] if 2 < len(i) else None,
                                       i[3] if 3 < len(i) else None))
    comb2 = runesCombListHelper(rarity2)
    for i in list(comb2):
        runes_list2.append(createRunes(rarity2, level2, i[0], i[1],
                                       i[2] if 2 < len(i) else None,
                                       i[3] if 3 < len(i) else None))
    return runes_list1, runes_list2


def runesCombListHelper(rarity):
    comb = []
    if rarity < 15:
        comb = product(rune_list, rune_list)
    if 15 <= rarity < 30:
        comb = product(rune_list, rune_list, rune_list)
    if 30 <= rarity:
        comb = product(rune_list, rune_list, rune_list, rune_list)
    return comb
