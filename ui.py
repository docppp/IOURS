from tkinter import *
import tkinter.ttk as ttk
import tkinter as tk
import tkinter.messagebox

from uiframes.framepet import FramePet
from uiframes.framerunes import FrameRunes
from uiframes.frameopponent import FrameOpponent
from uiframes.framehowto import FrameHowTo
from uiframes.frameplot import FramePlot

from load import loadThings
from ioumath import getBestRunes
from utils import saveFromTextBoxToFile
from plot import plotHeals


class IoursUi:
    def __init__(self, master=None):
        # build ui
        self.root = ttk.Frame(master)
        self.root.configure(height='200', width='200')
        self.root.pack(expand='true', ipadx='10', ipady='10', padx='10', pady='10', side='top')

        self.Inputframe = ttk.Frame(self.root)
        self.Inputframe.configure(height='200', width='200')
        self.Inputframe.pack(expand='true', side='top')

        self.Petframe = FramePet(self.Inputframe)
        self.Runesframe = FrameRunes(self.Inputframe)
        self.OpponentFrame = FrameOpponent(self.Inputframe, self.buttonCallback)
        self.HowToFrame = FrameHowTo(self.Inputframe)

        self.Outputframe = ttk.Frame(self.root)
        self.Outputframe.configure(height='200', width='200')
        self.Outputframe.pack(side='top')

        self.PlotFrame = FramePlot(self.Outputframe)

        # Main widget
        self.mainwindow = self.root

    def run(self):
        self.mainwindow.mainloop()

    # TODO
    # Better error handling
    def buttonCallback(self):
        if not saveFromTextBoxToFile(self.Petframe.text1, self.Petframe.text2, self.Petframe.entry1):
            tkinter.messagebox.showinfo("Error", "There were some error during saving data to iou.txt")
            return False

        try:
            pet1, pet2, bonus, runes = loadThings()
        except Exception:
            tkinter.messagebox.showinfo("Error", "There were some error during data parsing")
            return False

        params = {
            'pet1': pet1,
            'pet2': pet2,
            'bonus': bonus,
            'runes': runes,
            'rune1_rarity': int(self.Runesframe.spinbox_r1r.get()),
            'rune1_level': int(self.Runesframe.spinbox_r1l.get()),
            'rune2_rarity': int(self.Runesframe.spinbox_r2r.get()),
            'rune2_level': int(self.Runesframe.spinbox_r2l.get()),
            'opponent_level': int(self.OpponentFrame.spinbox_op.get())
        }

        if self.OpponentFrame.var_radio.get() == 0:
            buttonOneLevelClicked(params)
        if self.OpponentFrame.var_radio.get() == 1:
            buttonContinuousClicked(params)


def buttonOneLevelClicked(params):
    try:
        rune1, rune2, heals = getBestRunes(params['pet1'], params['pet2'], params['bonus'],
                                           params['rune1_rarity'], params['rune1_level'],
                                           params['rune2_rarity'], params['rune2_level'],
                                           params['opponent_level'])
        tkinter.messagebox.showinfo(f"Best Rune for level {params['opponent_level']}",
                                    f"First Rune:\t{rune1.__repr__()}\n"
                                    f"Second Rune:\t{rune2.__repr__()}\n"
                                    f"Used heals:\t{heals}")
    except Exception:
        tkinter.messagebox.showinfo("Error", "There were some error during calculations")
        return False

    return True


def buttonContinuousClicked(params):
    pass


