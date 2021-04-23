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

def fight(pet1, pet2, bonus, runes, op):
    const()
    favor_stack = 1
    anger_stack = 1
    pet1Damage = pet1.dmg
    pet2Damage = pet2.dmg
    pet1HP = pet1.hp
    pet2HP = pet2.hp
    opponentHp = op.hp
    shield = op.shield

    usedHeals = 0

    for i in range(1, const.max_rounds):
        # Before the fight
        if shield > 0:
            pet1Damage = int(pet1Damage*const.shield_reduction)
            pet2Damage = int(pet2Damage*const.shield_reduction)

        pet1Reflect = min(pet1Damage/2, op.base_dmg * bonus.reflect)
        pet2Reflect = min(pet2Damage/2, op.base_dmg * bonus.reflect)
        converge = (pet1Damage + pet2Damage) * bonus.converge

        # Regen
        pet1HP += (pet1.regen if i <= const.max_regen else 0)
        pet2HP += (pet2.regen if i <= const.max_regen else 0)

        # Fight
        damage = pet1Damage + pet1Reflect + pet2Damage + pet2Reflect + converge
        opponentHp -= damage

        # Pets below 0 hp do not receive any damage. If one pet is dead the other one will take double damage.
        d1 = int(op.dmg * (2 if pet2HP <= 0 else 1) / favor_stack)
        d2 = int(op.dmg * (2 if pet1HP <= 0 else 1) / favor_stack)
        pet1HP -= d1
        pet2HP -= d2

        # Heal
        while (usedHeals < const.max_heals) and (pet1HP <= 0 or pet2HP <= 0):
            pet1HP += pet1.heal
            pet2HP += pet2.heal
            usedHeals += 1

        # Exit condition
        if opponentHp <= 0:
            break

        # After fight
        poison_stack = 1 + (runes.poison * (i % (const.max_poison + 1)))
        anger_stack += runes.anger if i <= const.max_anger else 0
        favor_stack += runes.favor if i <= const.max_favor else 0
        shield = shield - const.pierce if shield > const.pierce else 0

        # Update pet dmg
        pet1Damage = int(pet1.dmg * poison_stack * anger_stack)
        pet2Damage = int(pet2.dmg * poison_stack * anger_stack)

    return usedHeals


def const():
    const.max_rounds = 1000
    const.max_favor = 5
    const.max_regen = 30
    const.max_poison = 5
    const.max_anger = 5
    const.max_heals = 2500
    const.pierce = 1
    const.shield_reduction = 0.02
