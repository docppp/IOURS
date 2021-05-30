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

rune_list = ['adrenaline', 'anger', 'favor', 'frenzy', 'poison', 'regen']


def getRunesFirstBonus(rarity, level, arena, name):
    return (1 + (rarity * scaling['rarity'] + level) * scaling['level']) / 100 * efficiency[name] * (1+arena)


def getRunesSecondBonus(rarity, level, arena, name):
    return (1 + (rarity * scaling['rarity'] + level) * scaling['level']) / 100 * efficiency[name] / 2 * (1+arena)


def getRunesThirdBonus(rarity, level, arena, name):
    return (1 + (rarity * scaling['rarity'] + level) * scaling['level']) / 100 * efficiency[name] / 4 * (1+arena)


def getRunesFourthBonus(rarity, level, arena, name):
    return (1 + (rarity * scaling['rarity'] + level) * scaling['level']) / 100 * efficiency[name] / 4 * (1+arena)


def createRunes(rarity, level, arena, first_bonus, second_bonus, third_bonus=None, fourth_bonus=None):
    runes = Runes()
    runes.arena = arena
    runes.adrenaline = 0
    runes.anger = 0
    runes.favor = 0
    runes.frenzy = 0
    runes.poison = 0
    runes.regen = 0
    runes.__setattr__(first_bonus, runes.__dict__.get(first_bonus)
                      + getRunesFirstBonus(rarity, level, arena, first_bonus))
    runes.__setattr__(second_bonus, runes.__dict__.get(second_bonus)
                      + getRunesSecondBonus(rarity, level, arena, second_bonus))
    runes.first = first_bonus
    runes.second = second_bonus

    if third_bonus:
        runes.__setattr__(third_bonus, runes.__dict__.get(third_bonus)
                          + getRunesThirdBonus(rarity, level, arena, third_bonus))
        runes.third = third_bonus

    if fourth_bonus:
        runes.__setattr__(fourth_bonus,
                          runes.__dict__.get(fourth_bonus)
                          + getRunesFourthBonus(rarity, level, arena, fourth_bonus))
        runes.fourth = fourth_bonus

    return runes


def runesCombList(rarity1, level1, rarity2, level2, arena):
    runes_list1 = []
    comb1 = runesCombListHelper(rarity1)
    for i in list(comb1):
        runes_list1.append(createRunes(rarity1, level1, arena, i[0], i[1],
                                       i[2] if 2 < len(i) else None,
                                       i[3] if 3 < len(i) else None))

    runes_list2 = []
    comb2 = runesCombListHelper(rarity2)
    for i in list(comb2):
        runes_list2.append(createRunes(rarity2, level2, arena, i[0], i[1],
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
