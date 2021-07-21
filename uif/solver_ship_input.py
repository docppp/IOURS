import tkinter.ttk as ttk
from uif.frame_ship_stats import FrameShipStats


class SolverShipInput:
    def __init__(self, master=None):
        self.root = ttk.Frame(master)
        self.root.configure(height='200', width='200')

        self.FrameShipStats = FrameShipStats(self.root)
