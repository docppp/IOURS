from copy import copy


class Pet:

    def __init__(self):
        self.dmg = 0
        self.hp = 0
        self.regen = 0
        self.reduced_regen = 0
        self.heal = 0

    def prepareForFight(self, opponent, bonus, runes):
        ret_pet = copy(self)
        ret_pet.dmg = int(ret_pet.dmg / opponent.defense * (1 + runes.frenzy) * (1 + runes.adrenaline * 0.1))
        ret_pet.hp = int(ret_pet.hp * (1 + runes.adrenaline))
        ret_pet.regen = int(ret_pet.hp * (bonus.regen + runes.regen))
        ret_pet.reduced_regen = int(ret_pet.hp * bonus.regen)
        ret_pet.heal = int(ret_pet.hp * bonus.heals)
        return ret_pet
