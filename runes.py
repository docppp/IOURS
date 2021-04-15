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

comb = product(rune_list, rune_list)
print(type(comb))


def createRunes(runes, rarity, level, first_rune, second_rune):
    runes.adrenaline = 0
    runes.anger = 0
    runes.favor = 0
    runes.frenzy = 0
    runes.poison = 0
    runes.regen = 0
    runes.__setattr__(first_rune, getRunesFirstBonus(rarity, level, first_rune))
    runes.__setattr__(second_rune, getRunesSecondBonus(rarity, level, second_rune))
    return runes


def runesGenerator(rarity, level):
    runes = Runes()
    for i in list(comb):
        print(i[0], i[1])
        runes = createRunes(runes, rarity, level, i[0], i[1])
        yield runes


for i in runesGenerator(14, 7):
    print(i)
