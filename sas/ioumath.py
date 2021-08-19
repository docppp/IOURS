from .bonus import BonusChar
from .opponent import Opponent
from .ship import Ship
from .fight import fight


def getCheapestBuild(params, params_tk):
    number_of_middle = 1
    number_of_left = 2
    number_of_right = 3

    bonus_guild = params['ship_stats']
    bonus_char = BonusChar()
    bonus_char.loadSpinbox(params_tk['spinbox'])

    left_ship = Ship()
    left_ship.lvl_weapon = 0
    left_ship.lvl_reactor = 0
    left_ship.lvl_hull = 53
    left_ship.lvl_wings = 0

    middle_ship = Ship()
    middle_ship.lvl_weapon = 0
    middle_ship.lvl_reactor = 0
    middle_ship.lvl_hull = 84
    middle_ship.lvl_wings = 0

    right_ship = Ship()
    right_ship.lvl_weapon = 115
    right_ship.lvl_reactor = 2
    right_ship.lvl_hull = 118
    right_ship.lvl_wings = 125

    opponent = Opponent.generateOpponent(800)

    m_dict = middle_ship.createShipDict(number_of_middle, bonus_guild, bonus_char)
    l_dict = left_ship.createShipDict(number_of_left, bonus_guild, bonus_char)
    r_dict = right_ship.createShipDict(number_of_right, bonus_guild, bonus_char)
    a_dict = opponent.createShipDict()

    result = fight(l_dict, m_dict, r_dict, a_dict)
    print(result)



