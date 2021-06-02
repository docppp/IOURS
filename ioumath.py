from copy import copy
from fight import fight
from runes import Runes
from ctypes import *
from multiprocessing import Pool, Lock, cpu_count
from opponent import Opponent

try:
    dll = CDLL('./fight.dll')
except FileNotFoundError:
    pass


min_heals = 99999999
rcopy1 = 'er'
rcopy2 = 'er'
lock = Lock()


# def preparePet(pet, opponent, bonus, runes):
#     lock.acquire()
#     ret_pet = copy(pet)
#     lock.release()
#     ret_pet.dmg = int(ret_pet.dmg / opponent.defense * (1 + runes.frenzy) * (1 + runes.adrenaline * 0.1))
#     ret_pet.hp = int(ret_pet.hp * (1 + runes.adrenaline))
#     ret_pet.regen = int(ret_pet.hp * (bonus.regen + runes.regen))
#     ret_pet.reduce_regen = int(ret_pet.hp * bonus.regen)
#     ret_pet.heal = int(ret_pet.hp * bonus.heals)
#     return ret_pet


def calculateHeals(pet1, pet2, bonus, runes, level):
    op = Opponent.generateOpponent(level, bonus.armor, runes.frenzy)
    p1 = pet1.prepareForFight(op, bonus, runes)
    p2 = pet2.prepareForFight(op, bonus, runes)
    # return fight(p1, p2, bonus, runes, op) # python implementation of fight

    pet1_dmg = c_longlong(p1.dmg)
    pet1_hp = c_longlong(p1.hp)
    pet2_dmg = c_longlong(p2.dmg)
    pet2_hp = c_longlong(p2.hp)

    bonus_reflect = c_float(bonus.reflect)
    bonus_converge = c_float(bonus.converge)
    runes_poison = c_float(runes.poison)
    runes_anger = c_float(runes.anger)
    runes_favor = c_float(runes.favor)

    op_hp = c_longlong(op.hp)
    op_base_dmg = c_longlong(op.base_dmg)
    op_shield = c_float(op.shield)

    ret = dll.fight(pet1_dmg, pet1_hp, p1.regen, p1.reduced_regen, p1.heal,
                    pet2_dmg, pet2_hp, p2.regen, p2.reduced_regen, p2.heal,
                    bonus_reflect, bonus_converge,
                    runes_poison, runes_anger, runes_favor,
                    op_hp, op_shield, op_base_dmg, op.dmg)
    return ret


def getBestRunes(params, progressbar=None, rounds=1, iter=0):
    global min_heals
    global rcopy1
    global rcopy2
    min_heals = 99999999
    rcopy1 = 'er'
    rcopy2 = 'er'
    list_rune1, list_rune2 = Runes.runesCombList(params['rune1_rarity'], params['rune1_level'],
                                                 params['rune2_rarity'], params['rune2_level'], params['arena'])
    part_done = 100 / rounds
    q = []
    with Pool(processes=cpu_count()) as pool:
        r = pool.map_async(getBestRunesHelper, [(x, y, params) for x in list_rune1 for y in list_rune2])
        while True:
            if r.ready():
                break
            remaining = r._number_left
            progressbar['value'] = part_done * iter + (part_done / remaining if remaining != 0 else part_done)
            progressbar.master.update_idletasks()
        q.append(r.get())
        r.wait()

    q = [x for x in q[0] if x is not None]
    q = min(q, key=lambda x: x[len(x) - 1])
    rcopy1, rcopy2, min_heals = q[0], q[1], q[2]
    return rcopy1, rcopy2, min_heals


def getBestRunesHelper(param_tuple):
    global min_heals
    global rcopy1
    global rcopy2
    global lock
    rune1, rune2 = param_tuple[0], param_tuple[1]
    params = param_tuple[2]
    rune = rune1 + rune2
    cur_heals = calculateHeals(params['pet1'], params['pet2'], params['bonus'], rune, params['opponent_level'])
    lock.acquire()
    if cur_heals < min_heals:
        min_heals = cur_heals
        rcopy1 = copy(rune1)
        rcopy2 = copy(rune2)
        lock.release()
        return rcopy1, rcopy2, min_heals
    lock.release()
    return None
