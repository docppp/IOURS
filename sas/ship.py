from math import floor
from .bonus import BonusGuild
from .bonus import BonusChar
from .const_tables import *


class Ship:

    def __init__(self):
        self.lvl_weapon = 0
        self.lvl_reactor = 0
        self.lvl_hull = 0
        self.lvl_wings = 0

    def createShipDict(self, number: int, guild: BonusGuild, char: BonusChar):
        hp = table_base_hps[self.lvl_hull]*(1+char.trophy_hp)*(1+char.asc_hp)*(1+char.orb_total)*(1+guild.space_academy)
        ship_dict = {
            'speed': (10+0.8*self.lvl_wings)*(1+floor(self.lvl_wings/5)/20),
            'armor': table_base_shl[self.lvl_reactor],
            'hp': hp,
            'dmg': table_base_dmg[self.lvl_weapon]*(1+char.trophy_dmg)*(1+char.asc_dmg)*(1+char.legendary)*(1+char.orb_total)*(1+guild.space_academy)*(1+guild.guild_passive),
            'armor_pen': 1.4250,
            'regen_hp': hp * 0.055,
            'leech': 0.4150,
            'absorb': self.lvl_reactor*0.02+0,
            'reflection': 0.2800,
            'number': number,
        }
        return ship_dict

    def calculateCost(self):
        ultinum = table_cost_ult[self.lvl_weapon] + \
                  table_cost_ult[self.lvl_reactor] + \
                  table_cost_ult[self.lvl_hull] + \
                  table_cost_ult[self.lvl_wings]
        imatter = table_cost_ima[self.lvl_weapon] + \
                  table_cost_ima[self.lvl_reactor] + \
                  table_cost_ima[self.lvl_hull] + \
                  table_cost_ima[self.lvl_wings]

        return ultinum, imatter




