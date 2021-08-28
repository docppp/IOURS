import unittest
from sas.bonus import BonusChar, BonusGuild
from sas.opponent import Opponent
from sas.ship import Ship
from sas.fight import fight


class TestFightShip(unittest.TestCase):

    def test_fight(self):
        bc = BonusChar()
        bc.virtue = 75
        bc.orb_star = 7
        bc.orb_level = 0
        bc.orb_total = (0.02*pow(7, 2)+0/100*(0.08*7+0.04)*0.4)*(1+75*0.005)
        bc.legendary = 0.5
        bc.asc_dmg = 0.2
        bc.asc_hp = 0.2
        bc.trophy_hp = 1
        bc.trophy_dmg = 1

        bg = BonusGuild()
        bg.space_academy = 7.4090
        bg.guild_passive = 1.1480

        num_left = 2
        num_midl = 1
        num_righ = 3

        def _shipFromValues(w, r, h, g):
            ship = Ship()
            ship.lvl_weapon = w
            ship.lvl_reactor = r
            ship.lvl_hull = h
            ship.lvl_wings = g
            return ship

        def _checkResultFromValueLists(left, midl, righ, ai_lvl, expected):
            l = _shipFromValues(left[0], left[1], left[2], left[3]).createShipDict(num_left, bg, bc)
            m = _shipFromValues(midl[0], midl[1], midl[2], midl[3]).createShipDict(num_midl, bg, bc)
            r = _shipFromValues(righ[0], righ[1], righ[2], righ[3]).createShipDict(num_righ, bg, bc)
            a = Opponent.generateOpponent(ai_lvl).createShipDict()
            result = fight(l, m, r, a)
            self.assertAlmostEqual(result, expected, 2)

        # probable scenario
        left = [0, 0, 40, 0]
        middle = [0, 0, 60, 0]
        right = [120, 20, 120, 130]

        ai_levels = [570, 580, 600, 650]
        expected = [-1, 90833.05, 101305.80, 153841.22]
        for i in range(4):
            _checkResultFromValueLists(left, middle, right, ai_levels[i], expected[i])

        # random scenario
        left = [25, 70, 15, 60]
        middle = [60, 0, 60, 190]
        right = [10, 0, 80, 80]

        ai_levels = [450, 460, 465, 600]
        expected = [-1, 43605.99, 52339.82, 136371.06]
        for i in range(4):
            _checkResultFromValueLists(left, middle, right, ai_levels[i], expected[i])




