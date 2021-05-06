from copy import copy
from functools import lru_cache
from math import floor
from fight import fight
from runes import runesCombList
from utils import auto_str
from ctypes import *
from multiprocessing import Pool, Lock, cpu_count

try:
    dll = CDLL('./fight.dll')
except FileNotFoundError:
    pass


@auto_str
class Opponent:
    def __init__(self, **kwargs):
        pass


@lru_cache(maxsize=None)
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
                       dmg_mod) * 2.5 * (1 + runes_frenzy * 0.1) * 0.70)
    op.dmg = round(op.base_dmg * bonus_armor / 2)
    return op


def preparePet(pet, opponent, bonus, runes):
    ret_pet = copy(pet)
    ret_pet.dmg = int(pet.dmg / opponent.defense * (1 + runes.frenzy) / (1 + runes.adrenaline * 0.1))
    ret_pet.regen = int(pet.hp * (bonus.regen + runes.regen))
    ret_pet.heal = int(pet.hp * bonus.heals)
    return ret_pet


def calculateHeals(pet1, pet2, bonus, runes, level):
    op = generateOpponent(level, bonus.armor, runes.frenzy)
    p1 = preparePet(pet1, op, bonus, runes)
    p2 = preparePet(pet2, op, bonus, runes)
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

    ret = dll.fight(pet1_dmg, pet1_hp, p1.regen, p1.heal,
                    pet2_dmg, pet2_hp, p2.regen, p2.heal,
                    bonus_reflect, bonus_converge,
                    runes_poison, runes_anger, runes_favor,
                    op_hp, op_shield, op_base_dmg, op.dmg)
    return ret


min_heals = 99999999
rcopy1 = 'er'
rcopy2 = 'er'
lock = Lock()


def getBestRunes(params, progressbar=None, rounds=1, iter=0):
    global min_heals
    global rcopy1
    global rcopy2
    min_heals = 99999999
    rcopy1 = 'er'
    rcopy2 = 'er'
    list_rune1, list_rune2 = runesCombList(params['rune1_rarity'], params['rune1_level'],
                                           params['rune2_rarity'], params['rune2_level'])
    part_done = 100/rounds
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
