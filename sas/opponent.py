from functools import lru_cache
from math import floor


class Opponent:

    def __init__(self):
        self.level = 0
        self.health = 0
        self.shield = 0
        self.eff_shield = 0
        self.dmg = 0
        self.speed = 0

    @staticmethod
    @lru_cache(maxsize=None)
    def generateOpponent(lvl):
        op = Opponent()
        op.level = lvl
        op.health = (60+20*(lvl-1+max(0, lvl-500)))*(1+floor((lvl-1)/5)/20)
        op.shield = (0+10*(lvl-1+max(0, lvl-500)))*(1+floor((lvl-1)/5)/20)
        op.eff_shield = op.shield*(1+(lvl/50))
        op.dmg = (10+2.5*(lvl-1+max(0, lvl-500)))*(1+floor((lvl-1)/5)/20)
        op.speed = (10+0.8*(lvl-1+max(0, lvl-500)))*(1+floor((lvl-1)/5)/20)
        return op

    def createShipDict(self):
        ship_dict = {
            'speed': self.speed,
            'armor': self.shield,
            'hp': self.health,
            'dmg': self.dmg,
            'armor_pen': 1,
            'regen_hp': 0,
            'leech': 0,
            'absorb': (self.level-1)*0.02,
            'reflection': 0,
            'number': 4
        }
        return ship_dict

