from load import loadThings
from utils import generateOpponent, preparePet
from fight import fight


pet1, pet2, bonus, runes = loadThings()


runes.favor = 0.074
runes.frenzy = 0.74
runes.poison = 0.0975
runes.regen = 0.26


def calculateHeals(pet1, pet2, bonus, runes, level):
    op = generateOpponent(level, bonus.armor, runes.frenzy)
    print(op)
    preparePet(pet1, op, bonus, runes)
    preparePet(pet2, op, bonus, runes)
    print(pet1)
    print(pet2)
    return fight(pet1, pet2, bonus, runes, op)


print(calculateHeals(pet1, pet2, bonus, runes, 290))
