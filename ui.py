import tkinter.ttk as ttk
import tkinter.messagebox
import time

from uiframes.framepet import FramePet
from uiframes.framerunes import FrameRunes
from uiframes.frameopponent import FrameOpponent
from uiframes.framehowto import FrameHowTo
from uiframes.frameplot import FramePlot


from rns.ioumath import getBestRunes
from utils import saveFromTextBoxToFile
from ldr.loader_master import LoaderMaster


class IoursUi:
    def __init__(self, master=None):
        # build ui
        self.root = ttk.Frame(master)
        self.root.configure(height='200', width='200')
        self.root.pack(expand='true', ipadx='0', ipady='0', padx='10', pady='10', side='top')

        self.Inputframe = ttk.Frame(self.root)
        self.Inputframe.configure(height='200', width='200')
        self.Inputframe.grid(column='0', row='0')

        self.Petframe = FramePet(self.Inputframe)
        self.Runesframe = FrameRunes(self.Inputframe)
        self.OpponentFrame = FrameOpponent(self.Inputframe, self.buttonCallback)
        self.HowToFrame = FrameHowTo(self.Inputframe)
        self.label = ttk.Label(self.Inputframe)
        self.label.configure(text='IOURS\nIdle Online Universe\nRunes Solver', justify='center',
                             font=('Arial', 12, 'bold'))
        self.label.grid(column='1', pady='5', row='1')

        self.Outputframe = ttk.Frame(self.root)
        self.Outputframe.configure(height='200', width='200')
        self.Outputframe.grid(column='1', row='0')
        self.PlotFrame = FramePlot(self.Outputframe)

        self.progress = ttk.Progressbar(self.root, mode='determinate', length=1200, maximum=110)
        self.progress.grid(column='0', row='1', columnspan='2')

        # Main widget
        self.mainwindow = self.root

    def run(self):
        self.mainwindow.mainloop()

    # TODO
    # Better error handling
    def buttonCallback(self):
        if not saveFromTextBoxToFile(self.Petframe.text1, self.Petframe.text2, self.Petframe.entry1,
                                     self.Runesframe, self.OpponentFrame):
            tkinter.messagebox.showinfo("Error", "There were some error during saving data to iou.txt")
            return False

        # try:
        loader = LoaderMaster()
        loader.re()
        pet1, pet2 = loader.pets.pets
        bonus = loader.pets.bonus
        runes = loader.pets.runes
        # except Exception:
        #     tkinter.messagebox.showinfo("Error", "There were some error during data parsing")
        #     return False

        params = {
            'pet1': pet1,
            'pet2': pet2,
            'bonus': bonus,
            'runes': runes,
            'rune1_rarity': int(self.Runesframe.spinbox_r1r.get()),
            'rune1_level': int(self.Runesframe.spinbox_r1l.get()),
            'rune2_rarity': int(self.Runesframe.spinbox_r2r.get()),
            'rune2_level': int(self.Runesframe.spinbox_r2l.get()),
            'opponent_level': int(self.OpponentFrame.spinbox_op.get()),
            'arena': runes.arena
        }
        capped = self.OpponentFrame.var_check.get()

        start = time.time()
        if self.OpponentFrame.var_radio.get() == 0:
            buttonOneLevelClicked(self.progress, params)
        if self.OpponentFrame.var_radio.get() == 1:
            buttonContinuousClicked(self.PlotFrame, self.progress, params, int(self.OpponentFrame.spinbox_limit.get())+1, capped)
        stop = time.time()
        # print("T: ", stop - start)
        return


def buttonOneLevelClicked(progressbar, params):
    progressbar['value'] = 0.0
    progressbar.master.update_idletasks()
    try:
        rune1, rune2, heals = getBestRunes(params, progressbar)
        progressbar['value'] += 10
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


def buttonContinuousClicked(frame, progressbar, params, limit=30, capped=False):
    progressbar['value'] = 0.0
    progressbar.master.update_idletasks()
    set_of_runes = _getRunesSet(progressbar, params, int(limit/10))
    frame.plotHeals(params, set_of_runes, limit, capped)
    progressbar['value'] += 10
    progressbar.master.update_idletasks()


def _getRunesSet(progressbar, params, rounds):
    set_of_runes = set()
    set_of_names = set()

    def do_add(s, x):
        return len(s) != (s.add(x) or len(s))

    for i in range(rounds):
        params['opponent_level'] += i * 10
        rune1, rune2, heals = getBestRunes(params, progressbar, rounds, i)
        params['opponent_level'] -= i * 10
        if do_add(set_of_names, (rune1.__str__(), rune2.__str__())):
            do_add(set_of_runes, (rune1, rune2))
    return set_of_runes
