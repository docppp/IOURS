import tkinter.messagebox
from rns.ioumath import getBestRunes, calculateHeals
from sas.ioumath import getCheapestBuild


class CalculateCallback:

    def __init__(self, callback_type):
        self.callback_type = callback_type

    def do(self, params, params_tk):
        if self.callback_type == "PetsOneLevel":
            self.doPetsOneLevel(params, params_tk)
        if self.callback_type == "PetsContinuous":
            self.doPetsContinuous(params, params_tk)
        if self.callback_type == "ShipArena":
            self.doShipArena(params, params_tk)

    @staticmethod
    def doPetsOneLevel(params, params_tk):
        progressbar = params_tk['progress']
        progressbar['value'] = 0.0
        progressbar.master.update_idletasks()
        try:
            rune1, rune2, heals = getBestRunes(params, params_tk)
            progressbar['value'] = 110
            sidenote = "\n\nHeals above 250. You cannot win lol." if heals > 250 else ""
            tkinter.messagebox.showinfo(f"Best Rune for level {params['opponent_level']}",
                                        f"First Rune:\t{rune1.__str__()}\n"
                                        f"Second Rune:\t{rune2.__str__()}\n"
                                        f"Used heals:\t{heals}"
                                        f"{sidenote}")
        except Exception:
            tkinter.messagebox.showinfo("Error", "There were some error during calculations")
            return False
        return True

    @staticmethod
    def doPetsContinuous(params, params_tk):
        progressbar = params_tk['progress']
        progressbar['value'] = 0.0
        progressbar.master.update_idletasks()
        set_of_runes = CalculateCallback._getRunesSet(params, params_tk)
        levels_list = list(range(params['opponent_level'], params['opponent_level'] + params['limit']))
        heals_list = []
        labels = []
        for r in set_of_runes:
            rune = r[0] + r[1]
            heals_list_part = []
            label_part = r[0].__str__() + " + " + r[1].__str__()
            pet1, pet2 = params['pets']
            for i in levels_list:
                h = calculateHeals(pet1, pet2, params['bonus'], rune, i)
                heals_list_part.append(h if (h < 250 or params['capped'] == 0) else 250)
            heals_list.append(heals_list_part)
            labels.append(label_part)
        frame_plot = params_tk['plot_frame']
        frame_plot.plot(levels_list, heals_list, labels)
        progressbar['value'] = 110
        progressbar.master.update_idletasks()

    @staticmethod
    def _getRunesSet(params, params_tk):
        rounds = int(params['limit']/10)
        set_of_runes = set()
        set_of_names = set()

        def do_add(s, x):
            return len(s) != (s.add(x) or len(s))

        for i in range(rounds):
            params['opponent_level'] += i * 10
            rune1, rune2, heals = getBestRunes(params, params_tk, rounds, i)
            params['opponent_level'] -= i * 10
            if do_add(set_of_names, (rune1.__str__(), rune2.__str__())):
                do_add(set_of_runes, (rune1, rune2))
        return set_of_runes

    @staticmethod
    def doShipArena(params, params_tk):
        print(params)
        print(params_tk)
        getCheapestBuild(params, params_tk)
