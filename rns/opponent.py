from functools import lru_cache
from math import floor


class Opponent:

    def __init__(self):
        self.level = 0
        self.hp = 0
        self.defense = 0
        self.shield = 0
        self.base_dmg = 0
        self.dmg = 0

    @staticmethod
    @lru_cache(maxsize=None)
    def generateOpponent(level, bonus_armor, runes_frenzy):
        op = Opponent()
        op.level = level
        bonus_diff = max(0, (op.level - 5) * 5) + max(0, (op.level - 10) * 2) + max(0, (op.level - 20) * 10)
        diff_mod = 5 + op.level * 5 + bonus_diff + op.level ** 2 / 5
        level_mod = floor(min(op.level, 30) / 5)
        mod5 = max(0, floor((op.level - 35) / 5))
        hp_mod = (1 + (max(0, op.level - 100)) ** 1.5 * 0.01) * (1.1 ** floor(op.level * 0.01) if op.level > 100 else 1)
        dmg_mod = (1 + (max(0, op.level - 100)) ** 1.5 * 0.01) * (
            1.1 ** floor(op.level * 0.003) if op.level > 100 else 1)
        op.hp = round(diff_mod * (op.level + 1) ** 2 * (
                min(1.0, 0.15 + 0.1 * level_mod) + (max(0, op.level - 35) + mod5) / 50) * hp_mod * 0.8)
        op.defense = 1 + max(0, op.level - 250) * 0.01 + (1 + (op.level - 500) * 0.1 if op.level > 500 else 0)
        op.shield = int(floor(max(0, op.level - 450) * 0.1) * (1 + max(0, op.level - 500) * 0.1))
        op.base_dmg = int((5 + (op.level + 1) ** 1.6 *
                           (0.15 + (0.085 * level_mod) + max(0, op.level - 35) * 0.1 + mod5 * 0.08) *
                           dmg_mod) * 2.5 * (1 + runes_frenzy * 0.1) * 0.70)
        op.dmg = round(op.base_dmg * bonus_armor / 2)
        return op
