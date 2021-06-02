from itertools import product


class Runes:

    def __init__(self):
        self.first: str = 'none'
        self.second: str = 'none'
        self.third: str = 'none'
        self.fourth: str = 'none'
        self.arena: float = 0
        self.adrenaline: float = 0
        self.anger: float = 0
        self.favor: float = 0
        self.frenzy: float = 0
        self.poison: float = 0
        self.regen: float = 0

    _scaling = {
        "rarity": 12,
        "level": 0.1,
    }

    _efficiency = {
        "adrenaline": 4,
        "anger": 1,
        "favor": 0.8,
        "frenzy": 4,
        "poison": 1.5,
        "regen": 2
    }

    _bonus_list = ['adrenaline', 'anger', 'favor', 'frenzy', 'poison', 'regen']

    def __add__(self, other):
        r = Runes()
        assert (self.arena == other.arena)
        r.arena = self.arena
        r.adrenaline = self.adrenaline + other.adrenaline
        r.anger = self.anger + other.anger
        r.favor = self.favor + other.favor
        r.frenzy = self.frenzy + other.frenzy
        r.poison = self.poison + other.poison
        r.regen = self.regen + other.regen
        return r

    def __str__(self):
        if self.fourth == 'none' and self.third == 'none':
            return f'{self.first}, {self.second}'
        if self.fourth == 'none':
            return f'{self.first}, {self.second}, {self.third}'
        return f'{self.first}, {self.second}, {self.third}, {self.fourth}'

    @staticmethod
    def _getRunesBonusValue(bonus_number, rarity, level, arena, name) -> float:
        """
        :return: Numeric value of n-th bonus in rune with respect to rarity, level and arena bonus
        """
        multiplier = 1 if bonus_number == 1 else 2 if bonus_number == 2 else 4
        return (1 + (rarity * Runes._scaling['rarity'] + level)
                * Runes._scaling['level']) / 100 * Runes._efficiency[name] / multiplier * (1 + arena)

    @staticmethod
    def createRunes(rarity, level, arena, first_bonus, second_bonus, third_bonus=None, fourth_bonus=None):
        """
        :return: Single rune with values of given bonuses and arena bonus
        """
        runes = Runes()
        runes.arena = arena
        runes.__setattr__(first_bonus, runes.__dict__.get(first_bonus)
                          + Runes._getRunesBonusValue(1, rarity, level, arena, first_bonus))
        runes.__setattr__(second_bonus, runes.__dict__.get(second_bonus)
                          + Runes._getRunesBonusValue(2, rarity, level, arena, second_bonus))
        runes.first = first_bonus
        runes.second = second_bonus

        if third_bonus:
            runes.__setattr__(third_bonus, runes.__dict__.get(third_bonus)
                              + Runes._getRunesBonusValue(3, rarity, level, arena, third_bonus))
            runes.third = third_bonus

        if fourth_bonus:
            runes.__setattr__(fourth_bonus,
                              runes.__dict__.get(fourth_bonus)
                              + Runes._getRunesBonusValue(4, rarity, level, arena, fourth_bonus))
            runes.fourth = fourth_bonus

        return runes

    @staticmethod
    def runesCombList(rarity1, level1, rarity2, level2, arena) -> [list, list]:
        """
        :return: Two lists with all possible runes which bonuses respect level and rarity values with arena bonus
        """
        runes_list1 = []
        comb1 = Runes._runesCombListHelper(rarity1)
        for i in list(comb1):
            runes_list1.append(Runes.createRunes(rarity1, level1, arena, i[0], i[1],
                                                 i[2] if 2 < len(i) else None,
                                                 i[3] if 3 < len(i) else None))

        runes_list2 = []
        comb2 = Runes._runesCombListHelper(rarity2)
        for i in list(comb2):
            runes_list2.append(Runes.createRunes(rarity2, level2, arena, i[0], i[1],
                                                 i[2] if 2 < len(i) else None,
                                                 i[3] if 3 < len(i) else None))

        return runes_list1, runes_list2

    @staticmethod
    def _runesCombListHelper(rarity) -> list:
        """
        :return: list off all possible bonus combination in rune with given rarity
        """
        comb = []
        if rarity < 15:
            comb = product(Runes._bonus_list, Runes._bonus_list)
        if 15 <= rarity < 30:
            comb = product(Runes._bonus_list, Runes._bonus_list, Runes._bonus_list)
        if 30 <= rarity:
            comb = product(Runes._bonus_list, Runes._bonus_list, Runes._bonus_list, Runes._bonus_list)
        return comb
