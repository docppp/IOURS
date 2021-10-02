import tkinter.ttk as ttk
from uif.frame_runes_plot import FramePlot


class SolverRunesOutput:
    def __init__(self, master=None):
        self.root = ttk.Frame(master)
        self.root.configure(height='200', width='200')

        self.PlotFrame = FramePlot(self.root)
