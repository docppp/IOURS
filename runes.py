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
    return (1+(rarity*scaling['rarity']+level)*scaling['level'])/100*efficiency[name]


def getRunesSecondBonus(rarity, level, name):
    return (1+(rarity*scaling['rarity']+level)*scaling['level'])/100*efficiency[name]/2


rune_list = ['adrenaline', 'anger', 'favor', 'frenzy', 'poison', 'regen']




def createRunes(rarity, level, first_rune, second_rune):
    runes = Runes()
    runes.adrenaline = 0
    runes.anger = 0
    runes.favor = 0
    runes.frenzy = 0
    runes.poison = 0
    runes.regen = 0
    runes.__setattr__(first_rune, runes.__dict__.get(first_rune) + getRunesFirstBonus(rarity, level, first_rune))
    runes.__setattr__(second_rune, runes.__dict__.get(second_rune) + getRunesSecondBonus(rarity, level, second_rune))
    runes.first = first_rune
    runes.second = second_rune
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
    comb = product(rune_list, rune_list)
    for i in list(comb):
        runes_list1.append(createRunes(rarity1, level1, i[0], i[1]))
        runes_list2.append(createRunes(rarity2, level2, i[0], i[1]))
    return runes_list1, runes_list2
