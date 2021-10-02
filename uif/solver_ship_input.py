import tkinter.ttk as ttk
from uif.frame_ship_stats import FrameShipStats
from uif.frame_ship_guild import FrameShipGuild


class SolverShipInput:
    def __init__(self, master=None):
        self.root = ttk.Frame(master)
        self.root.configure(height='200', width='200')

        self.FrameShipStats = FrameShipStats(self.root)
        self.FrameShipStats.root.grid(column='0', ipadx='5', ipady='5', row='0')

        self.FrameShipGuild = FrameShipGuild(self.root)
        self.FrameShipGuild.root.grid(column='1', ipadx='5', ipady='5', row='0', sticky='n')
