from math import ceil


def round(n, decimals=0):
    multiplier = 10 ** decimals
    return ceil(n * multiplier) / multiplier


deadly_inc_a = 0.27
deadly_inc_b = 0
ArenaO41 = 1.5

# middle_ship_stats = {
#     'speed': 10,
#     'armor': 0,
#     'hp': 1347294.49,
#     'dmg': 1366.377989,
#     'armor_pen': 1.4250,
#     'regen_hp': 74101.2,
#     'leech': 0.4150,
#     'absorb': 0,
#     'reflection': 0.2800,
#     'number': 1
# }
#
# left_ship_stats = {
#     'speed': 10,
#     'armor': 0,
#     'hp': 71245.03,
#     'dmg': 1366.377989,
#     'armor_pen': 1.4250,
#     'regen_hp': 3918.48,
#     'leech': 0.4150,
#     'absorb': 0,
#     'reflection': 0.2800,
#     'number': 2
# }
#
# right_ship_stats = {
#     'speed': 247.5,
#     'armor': 0,
#     'hp': 220647.56,
#     'dmg': 87396.95209,
#     'armor_pen': 1.4250,
#     'regen_hp': 12135.62,
#     'leech': 0.4150,
#     'absorb': 0,
#     'reflection': 0.2800,
#     'number': 3
# }
#
# ai_ship_stats = {
#     'speed': 7958.34,
#     'armor': 98360.5,
#     'hp': 197258.00,
#     'dmg': 24679.625,
#     'armor_pen': 1,
#     'regen_hp': 0,
#     'leech': 0,
#     'absorb': 15.98,
#     'reflection': 0,
#     'number': 4
# }


def fight(left_ship_stats, middle_ship_stats, right_ship_stats, ai_ship_stats):
    global_attack_time = max(middle_ship_stats['speed'],
                             right_ship_stats['speed'],
                             ai_ship_stats['speed']) * 10

    middle_ship = {
        'attack_timer': [0],
        'armor': [middle_ship_stats['armor']],
        'hp': [middle_ship_stats['hp']],
        'dmg_armor': [0],
        'dmg_hp': [0],
        'reflect_armor': [0],
        'reflect_hp': [0],
        'hp_gain': [middle_ship_stats['regen_hp']],
        'armor_after': [middle_ship_stats['armor']],
        'hp_after': [middle_ship_stats['hp']],
    }

    left_ship = {
        'attack_timer': [global_attack_time],
        'armor': [left_ship_stats['armor']],
        'hp': [left_ship_stats['hp']],
        'dmg_armor': [0],
        'dmg_hp': [0],
        'reflect_armor': [0],
        'reflect_hp': [0],
        'hp_gain': [0],
        'armor_after': [left_ship_stats['armor']],
        'hp_after': [left_ship_stats['hp']],
    }

    right_ship = {
        'attack_timer': [global_attack_time],
        'armor': [right_ship_stats['armor']],
        'hp': [right_ship_stats['hp']],
        'dmg_armor': [0],
        'dmg_hp': [0],
        'reflect_armor': [0],
        'reflect_hp': [0],
        'hp_gain': [0],
        'armor_after': [right_ship_stats['armor']],
        'hp_after': [right_ship_stats['hp']],
    }

    ai_ship = {
        'attack_timer': [global_attack_time],
        'armor': [ai_ship_stats['armor']],
        'hp': [ai_ship_stats['hp']],
        'dmg_armor': [middle_ship_stats['dmg'] * middle_ship_stats['armor_pen'] / (1 + ai_ship_stats['absorb'])],
        'dmg_hp': [0],
        'reflect_armor': [0],
        'reflect_hp': [0],
        'hp_gain': [0],
        'armor_after': [ai_ship_stats['armor'] - middle_ship_stats['dmg'] * middle_ship_stats['armor_pen'] / (
                1 + ai_ship_stats['absorb'])],
        'hp_after': [ai_ship_stats['hp']],
    }

    interval = [0]
    timer = [0]
    casualties_a = [
        1 if middle_ship['hp'][0] <= 0 else 0 + 1 if left_ship['hp'][0] <= 0 else 0 + 1 if right_ship['hp'][0] <= 0 else 0]
    d_inc_dmg_a = [(casualties_a[0] * deadly_inc_a) + 1]
    casualties_b = [1 if ai_ship['hp'][0] <= 0 else 0]
    d_inc_dmg_b = [1]

    attacking_ship = [1]
    target_ship = [4]
    front_ship = [
        ((0 if right_ship['hp'][0] <= 0 else 3) if left_ship['hp'][0] <= 0 else 2) if middle_ship['hp'][0] <= 0 else 1]

    next_ship1 = [round(((middle_ship['attack_timer'][0] if middle_ship['attack_timer'][0] > 0 else
                          (middle_ship['attack_timer'][0] + global_attack_time)) / middle_ship_stats['speed']) if
                        middle_ship['hp'][0] > 0 else 999, 4)]
    next_ship2 = [round((left_ship['attack_timer'][0] if left_ship['attack_timer'][0] > 0 else
                         left_ship['attack_timer'][0] + global_attack_time) / left_ship_stats['speed'] if
                        left_ship['hp_after'][0] > 0 else 999, 4)]
    next_ship3 = [round((right_ship['attack_timer'][0] if right_ship['attack_timer'][0] > 0 else
                         right_ship['attack_timer'][0] + global_attack_time) / right_ship_stats['speed'] if
                        right_ship['hp_after'][0] > 0 else 999, 4)]
    next_ship4 = [round((ai_ship['attack_timer'][0] if ai_ship['attack_timer'][0] > 0 else
                         ai_ship['attack_timer'][0] + global_attack_time) / ai_ship_stats['speed'] if
                        ai_ship['hp_after'][0] > 0 else 999, 4)]
    selected_ship = [min(next_ship1[0], next_ship2[0], next_ship4[0], next_ship4[0])]

    def isSameTime(s1, s2, s3, s4, selected):
        x = 0
        x = x + 1 if s1[-1] == selected[-1] else x
        x = x + 1 if s2[-1] == selected[-1] else x
        x = x + 1 if s3[-1] == selected[-1] else x
        x = x + 1 if s4[-1] == selected[-1] else x
        if x > 1:
            if s1[-1] == selected[-1]:
                return 1
            if s2[-1] == selected[-1]:
                return 2
            if s3[-1] == selected[-1]:
                return 3
            return 4
        return 0

    same_time_ship = [isSameTime(next_ship1, next_ship2, next_ship3, next_ship4, selected_ship)]
    winner = [None]

    for r in range(0, 74):
        interval.append(0 if same_time_ship[-1] > 0 else selected_ship[-1])
        timer.append(timer[-1] + interval[-1])

        # Before Attack
        if r == 0:
            middle_ship['attack_timer'].append(round(middle_ship['attack_timer'][-1] - (middle_ship_stats['speed'] * (selected_ship[-1] if same_time_ship[-1] == 1 else interval[-1])) + (0 if middle_ship['attack_timer'][-1] > 0 else (global_attack_time * ArenaO41)), 2))
            left_ship['attack_timer'].append(round(left_ship['attack_timer'][-1] - (left_ship_stats['speed'] * (selected_ship[-1] if same_time_ship[-1] == 1 else interval[-1])) + (0 if left_ship['attack_timer'][-1] > 0 else global_attack_time), 2))
            right_ship['attack_timer'].append(round(right_ship['attack_timer'][-1] - (right_ship_stats['speed'] * (selected_ship[-1] if same_time_ship[-1] == 1 else interval[-1])) + (0 if right_ship['attack_timer'][-1] > 0 else global_attack_time), 2))
        else:
            middle_ship['attack_timer'].append(round(middle_ship['attack_timer'][-1] - (middle_ship_stats['speed'] * (selected_ship[-1] if same_time_ship[-1] == 1 else interval[-1])) + (0 if middle_ship['attack_timer'][-1] > 0 else (global_attack_time * ArenaO41 + (selected_ship[-1]*middle_ship_stats['speed'] if interval[-1] == 0 else 0))), 2))
            left_ship['attack_timer'].append(round(left_ship['attack_timer'][-1] - (left_ship_stats['speed'] * (selected_ship[-1] if same_time_ship[-1] == 1 else interval[-1])) + (0 if left_ship['attack_timer'][-1] > 0 else (global_attack_time + (selected_ship[-1]*left_ship_stats['speed'] if interval[-1] == 0 else 0))), 2))
            right_ship['attack_timer'].append(round(right_ship['attack_timer'][-1] - (right_ship_stats['speed'] * (selected_ship[-1] if same_time_ship[-1] == 1 else interval[-1])) + (0 if right_ship['attack_timer'][-1] > 0 else (global_attack_time + (selected_ship[-1]*right_ship_stats['speed'] if interval[-1] == 0 else 0))), 2))

        middle_ship['armor'].append(middle_ship['armor_after'][-1])
        middle_ship['hp'].append(middle_ship['hp_after'][-1])

        left_ship['armor'].append(left_ship['armor_after'][-1])
        left_ship['hp'].append(left_ship['hp_after'][-1])

        right_ship['armor'].append(right_ship['armor_after'][-1])
        right_ship['hp'].append(right_ship['hp_after'][-1])

        ai_ship['attack_timer'].append(round(ai_ship['attack_timer'][-1] - (ai_ship_stats['speed'] * interval[-1]) + (0 if ai_ship['attack_timer'][-1] > 0 else global_attack_time), 2))
        ai_ship['armor'].append(ai_ship['armor_after'][-1])
        ai_ship['hp'].append(ai_ship['hp_after'][-1])

        #  Attacking ship
        if middle_ship['hp'][-1] > 0 and middle_ship['attack_timer'][-1] <= 0:
            attacking_ship.append(1)
        if left_ship['hp'][-1] > 0 and left_ship['attack_timer'][-1] <= 0:
            attacking_ship.append(2)
        if right_ship['hp'][-1] > 0 and right_ship['attack_timer'][-1] <= 0:
            attacking_ship.append(3)
        if ai_ship['hp'][-1] > 0 and ai_ship['attack_timer'][-1] <= 0:
            attacking_ship.append(4)

        #  Front ship
        if middle_ship['hp'][-1] > 0:
            front_ship.append(1)
        elif left_ship['hp'][-1] > 0:
            front_ship.append(2)
        elif right_ship['hp'][-1] > 0:
            front_ship.append(3)
        if middle_ship['hp'][-1] <= 0 and left_ship['hp'][-1] <= 0 and right_ship['hp'][-1] <= 0:
            front_ship.append(0)

        #  Target ship
        target_ship.append(front_ship[-1] if attacking_ship[-1] == 4 else (4 if attacking_ship[-1] > 0 else 0))

        #  Next Attack Time
        next_ship1.append(round(((middle_ship['attack_timer'][-1] if middle_ship['attack_timer'][-1] > 0 else middle_ship['attack_timer'][-1] + global_attack_time) / middle_ship_stats['speed'] + (selected_ship[-1] if same_time_ship[-1] == 1 else 0)) if middle_ship['hp_after'][-1] > 0 else 999, 4))
        next_ship2.append(round(((left_ship['attack_timer'][-1] if left_ship['attack_timer'][-1] > 0 else left_ship['attack_timer'][-1] + global_attack_time) / left_ship_stats['speed'] + (selected_ship[-1] if same_time_ship[-1] == 2 else 0)) if left_ship['hp_after'][-1] > 0 else 999, 4))
        next_ship3.append(round(((right_ship['attack_timer'][-1] if right_ship['attack_timer'][-1] > 0 else right_ship['attack_timer'][-1] + global_attack_time) / right_ship_stats['speed'] + (selected_ship[-1] if same_time_ship[-1] == 3 else 0)) if right_ship['hp_after'][-1] > 0 else 999, 4))
        next_ship4.append(round(((ai_ship['attack_timer'][-1] if ai_ship['attack_timer'][-1] > 0 else ai_ship['attack_timer'][-1] + global_attack_time) / ai_ship_stats['speed']) if ai_ship['hp_after'][-1] > 0 else 999, 4))

        selected_ship.append(min(next_ship1[-1], next_ship2[-1], next_ship3[-1], next_ship4[-1]))
        same_time_ship.append(isSameTime(next_ship1, next_ship2, next_ship3, next_ship4, selected_ship))

        casualties_a.append((1 if middle_ship['hp'][-1] <= 0 else 0)
                            + (1 if left_ship['hp'][-1] <= 0 else 0)
                            + (1 if right_ship['hp'][-1] <= 0 else 0))

        d_inc_dmg_a.append(casualties_a[-1] * deadly_inc_a + 1)
        casualties_b.append(1 if ai_ship['hp'][-1] <= 0 else 0)
        d_inc_dmg_b.append(casualties_b[-1] * deadly_inc_b + 1)

        #  During Attack
        if middle_ship_stats['number'] == target_ship[-1]:
            middle_ship['dmg_armor'].append(ai_ship_stats['dmg'] * ai_ship_stats['armor_pen'] * d_inc_dmg_b[-1] / (1 + middle_ship_stats['absorb']))
            middle_ship['dmg_hp'].append(max(middle_ship['dmg_armor'][-1] - middle_ship['armor'][-1], 0) * (1 + middle_ship_stats['absorb']) * ai_ship_stats['armor_pen'])
        else:
            middle_ship['dmg_armor'].append(0)
            middle_ship['dmg_hp'].append(0)
        if middle_ship_stats['number'] == attacking_ship[-1]:
            middle_ship['reflect_armor'].append((min(ai_ship['dmg_armor'][-1], ai_ship['armor'][-1]) + ai_ship['dmg_hp'][-1]) * ai_ship_stats['reflection'] / (1 + middle_ship_stats['absorb']))
            middle_ship['reflect_hp'].append(max(middle_ship['reflect_armor'][-1] - middle_ship['armor'][-1], 0) * (1 + middle_ship_stats['absorb']))
            middle_ship['hp_gain'].append(middle_ship_stats['regen_hp'] + (ai_ship['dmg_hp'][-1] * middle_ship_stats['leech']))
        else:
            middle_ship['reflect_armor'].append(0)
            middle_ship['reflect_hp'].append(0)
            middle_ship['hp_gain'].append(0)

        if left_ship_stats['number'] == target_ship[-1]:
            left_ship['dmg_armor'].append(ai_ship_stats['dmg'] * ai_ship_stats['armor_pen'] * d_inc_dmg_b[-1] / (1 + left_ship_stats['absorb']))
            left_ship['dmg_hp'].append(max(left_ship['dmg_armor'][-1] - left_ship['armor'][-1], 0) * (1 + left_ship_stats['absorb']) * ai_ship_stats['armor_pen'])
        else:
            left_ship['dmg_armor'].append(0)
            left_ship['dmg_hp'].append(0)
        if left_ship_stats['number'] == attacking_ship[-1]:
            left_ship['reflect_armor'].append((min(ai_ship['dmg_armor'][-1], ai_ship['armor'][-1]) + ai_ship['dmg_hp'][-1]) * ai_ship_stats['reflection'] / (1 + left_ship_stats['absorb']))
            left_ship['reflect_hp'].append(max(left_ship['reflect_armor'][-1] - left_ship['armor'][-1], 0) * (1 + left_ship_stats['absorb']))
            left_ship['hp_gain'].append(left_ship_stats['regen_hp'] + (ai_ship['dmg_hp'][-1] * left_ship_stats['leech']))
        else:
            left_ship['reflect_armor'].append(0)
            left_ship['reflect_hp'].append(0)
            left_ship['hp_gain'].append(0)

        if right_ship_stats['number'] == target_ship[-1]:
            right_ship['dmg_armor'].append(ai_ship_stats['dmg'] * ai_ship_stats['armor_pen'] * d_inc_dmg_b[-1] / (1 + right_ship_stats['absorb']))
            right_ship['dmg_hp'].append(max(right_ship['dmg_armor'][-1] - right_ship['armor'][-1], 0) * (1 + right_ship_stats['absorb']) * ai_ship_stats['armor_pen'])
        else:
            right_ship['dmg_armor'].append(0)
            right_ship['dmg_hp'].append(0)
        if right_ship_stats['number'] == attacking_ship[-1]:
            right_ship['reflect_armor'].append((min(ai_ship['dmg_armor'][-1], ai_ship['armor'][-1]) + ai_ship['dmg_hp'][-1]) * ai_ship_stats['reflection'] / (1 + right_ship_stats['absorb']))
            right_ship['reflect_hp'].append(max(right_ship['reflect_armor'][-1] - right_ship['armor'][-1], 0) * (1 + right_ship_stats['absorb']))
            right_ship['hp_gain'].append(right_ship_stats['regen_hp'] + (ai_ship['dmg_hp'][-1] * right_ship_stats['leech']))
        else:
            right_ship['reflect_armor'].append(0)
            right_ship['reflect_hp'].append(0)
            right_ship['hp_gain'].append(0)

        if ai_ship_stats['number'] == target_ship[-1]:
            if attacking_ship[-1] == middle_ship_stats['number']:
                ai_ship['dmg_armor'].append(middle_ship_stats['dmg'] * middle_ship_stats['armor_pen'] / (1 + ai_ship_stats['absorb']) * d_inc_dmg_a[-1])
                ai_ship['dmg_hp'].append(max(ai_ship['dmg_armor'][-1]-ai_ship['armor'][-1], 0)*(1+ai_ship_stats['absorb'])/middle_ship_stats['armor_pen'])
            if attacking_ship[-1] == left_ship_stats['number']:
                ai_ship['dmg_armor'].append(left_ship_stats['dmg'] * left_ship_stats['armor_pen'] / (1 + ai_ship_stats['absorb']) * d_inc_dmg_a[-1])
                ai_ship['dmg_hp'].append(max(ai_ship['dmg_armor'][-1]-ai_ship['armor'][-1], 0)*(1+ai_ship_stats['absorb'])/left_ship_stats['armor_pen'])
            if attacking_ship[-1] == right_ship_stats['number']:
                ai_ship['dmg_armor'].append(right_ship_stats['dmg'] * right_ship_stats['armor_pen'] / (1 + ai_ship_stats['absorb']) * d_inc_dmg_a[-1])
                ai_ship['dmg_hp'].append(max(ai_ship['dmg_armor'][-1]-ai_ship['armor'][-1], 0)*(1+ai_ship_stats['absorb'])/right_ship_stats['armor_pen'])
            ai_ship['reflect_armor'].append(0)
            ai_ship['hp_gain'].append(0)
            ai_ship['reflect_hp'].append(0)
        if ai_ship_stats['number'] == attacking_ship[-1]:
            if target_ship[-1] == middle_ship_stats['number']:
                ai_ship['reflect_armor'].append(((min(middle_ship['dmg_armor'][-1], middle_ship['armor'][-1]) + middle_ship['dmg_hp'][-1]) * middle_ship_stats['reflection']) / (1 + ai_ship_stats['absorb']))
                ai_ship['hp_gain'].append(ai_ship_stats['regen_hp'] + middle_ship['dmg_hp'][-1] * ai_ship_stats['leech'])
            if target_ship[-1] == left_ship_stats['number']:
                ai_ship['reflect_armor'].append(((min(left_ship['dmg_armor'][-1], left_ship['armor'][-1]) + left_ship['dmg_hp'][-1]) * left_ship_stats['reflection']) / (1 + ai_ship_stats['absorb']))
                ai_ship['hp_gain'].append(ai_ship_stats['regen_hp'] + left_ship['dmg_hp'][-1] * ai_ship_stats['leech'])
            if target_ship[-1] == right_ship_stats['number']:
                ai_ship['reflect_armor'].append(((min(right_ship['dmg_armor'][-1], right_ship['armor'][-1]) + right_ship['dmg_hp'][-1]) * right_ship_stats['reflection']) / (1 + ai_ship_stats['absorb']))
                ai_ship['hp_gain'].append(ai_ship_stats['regen_hp'] + right_ship['dmg_hp'][-1] * ai_ship_stats['leech'])
            ai_ship['reflect_hp'].append(max(ai_ship['reflect_armor'][-1] - ai_ship['armor'][-1], 0) * (1 + ai_ship_stats['absorb']))
            ai_ship['dmg_armor'].append(0)
            ai_ship['dmg_hp'].append(0)

        #  After Attack
        middle_ship['armor_after'].append(max(middle_ship['armor'][-1]-middle_ship['dmg_armor'][-1]-middle_ship['reflect_armor'][-1], 0))
        middle_ship['hp_after'].append(min(middle_ship['hp'][-1]-middle_ship['dmg_hp'][-1]-middle_ship['reflect_hp'][-1]+middle_ship['hp_gain'][-1], middle_ship_stats['hp']))

        left_ship['armor_after'].append(max(left_ship['armor'][-1]-left_ship['dmg_armor'][-1]-left_ship['reflect_armor'][-1], 0))
        left_ship['hp_after'].append(min(left_ship['hp'][-1]-left_ship['dmg_hp'][-1]-left_ship['reflect_hp'][-1]+left_ship['hp_gain'][-1], left_ship_stats['hp']))

        right_ship['armor_after'].append(max(right_ship['armor'][-1]-right_ship['dmg_armor'][-1]-right_ship['reflect_armor'][-1], 0))
        right_ship['hp_after'].append(min(right_ship['hp'][-1]-right_ship['dmg_hp'][-1]-right_ship['reflect_hp'][-1]+right_ship['hp_gain'][-1], right_ship_stats['hp']))

        ai_ship['armor_after'].append(max(ai_ship['armor'][-1]-ai_ship['dmg_armor'][-1]-ai_ship['reflect_armor'][-1], 0))
        ai_ship['hp_after'].append(min(ai_ship['hp'][-1]-ai_ship['dmg_hp'][-1]-ai_ship['reflect_hp'][-1]+ai_ship['hp_gain'][-1], ai_ship_stats['hp']))

        #  Winner
        winner.append((("Ai" if attacking_ship[-1] == 4 else "Player") if next_ship4[-1] == 999 else "Ai") if next_ship1[-1]+next_ship2[-1]+next_ship3[-1] == 2997 else ("Player" if next_ship4[-1] == 999 else None))

        if winner[-1] == "Player":
            return "Player", 0
        if winner[-1] == "Ai":
            return "Ai", ai_ship['hp_after'][-1] + ai_ship['hp_after'][-1]

    return "Nobody"


