import tkinter.messagebox
from rns.ioumath import getBestRunes


class CalculateCallback:

    def __init__(self, callback_type):
        self.callback_type = callback_type

    def do(self, params):
        if self.callback_type == "PetsOneLevel":
            self.doPetsOneLevel(params)

    @staticmethod
    def doPetsOneLevel(params):
        progressbar = params['progress']
        progressbar['value'] = 0.0
        progressbar.master.update_idletasks()
        rune1, rune2, heals = getBestRunes(params)
        progressbar['value'] += 10
        sidenote = "\n\nHeals above 250. You cannot win lol." if heals > 250 else ""
        tkinter.messagebox.showinfo(f"Best Rune for level {params['opponent_level']}",
                                    f"First Rune:\t{rune1.__str__()}\n"
                                    f"Second Rune:\t{rune2.__str__()}\n"
                                    f"Used heals:\t{heals}"
                                    f"{sidenote}")