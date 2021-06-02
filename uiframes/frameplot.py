import tkinter as tk
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from rns.ioumath import calculateHeals

matplotlib.use("TkAgg")


class FramePlot:
    def __init__(self, master):
        self.master = master
        self.canvas = FigureCanvasTkAgg(None, self.master)
        self.canvas.get_tk_widget().pack(side='top')
        self.canvas.get_tk_widget().config(height=400, width=600)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.master)
        self.toolbar.children['!button'].pack_forget()
        self.toolbar.children['!button2'].pack_forget()
        self.toolbar.children['!button3'].pack_forget()
        self.toolbar.children['!button4'].pack_forget()

    def makePlot(self, f):
        self.canvas.get_tk_widget().pack_forget()
        self.toolbar.pack_forget()

        self.canvas = FigureCanvasTkAgg(f, self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.master)
        self.toolbar.update()
        self.toolbar.children['!button'].pack_forget()
        self.toolbar.children['!button2'].pack_forget()
        self.toolbar.children['!button3'].pack_forget()
        self.toolbar.children['!button4'].pack_forget()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.canvas.get_tk_widget().config(height=400, width=600)

    def plotHeals(self, params, set_of_runes, limit, capped):
        f = plt.figure()

        levels_list = list(range(params['opponent_level'], params['opponent_level'] + limit))
        for r in set_of_runes:
            rune = r[0] + r[1]
            heals_list = []
            label = r[0].__repr__() + " + " + r[1].__repr__()
            if capped:
                for i in levels_list:
                    h = calculateHeals(params['pet1'], params['pet2'], params['bonus'], rune, i)
                    heals_list.append(h if h < 250 else 250)
            else:
                for i in levels_list:
                    heals_list.append(calculateHeals(params['pet1'], params['pet2'], params['bonus'], rune, i))
            plt.plot(levels_list, heals_list, label=label)

        plt.grid(True)
        plt.legend(loc='best')
        plt.tight_layout()
        self.makePlot(f)
