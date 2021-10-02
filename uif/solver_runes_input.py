import tkinter.ttk as ttk
from uif.frame_runes_pet import FramePet
from uif.frame_runes_runes import FrameRunes
from uif.frame_runes_opponent import FrameOpponent
from uif.frame_runes_howto import FrameHowTo


class SolverRunesInput:
    def __init__(self, master=None):
        self.root = ttk.Frame(master)
        self.root.configure(height='200', width='200')

        self.PetFrame = FramePet(self.root)
        self.RunesFrame = FrameRunes(self.root)
        self.OpponentFrame = FrameOpponent(self.root)
        self.HowToFrame = FrameHowTo(self.root)
        self.HowToFrame.labelframe.grid(column='0', row='0', sticky='nw', columnspan='2')
        self.PetFrame.Framepet.grid(column='0', row='1', rowspan='2')
        self.RunesFrame.Framerunes.grid(column='1', row='1', sticky='nw')
        self.OpponentFrame.Frameopponent.grid(column='1', row='2', sticky='nw')
