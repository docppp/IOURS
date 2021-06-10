import tkinter.ttk as ttk
import tkinter.messagebox
from ldr.loader_master import LoaderMaster
from uif.calculate import CalculateCallback
from uif.solver_runes_input import SolverRunesInput
from uif.solver_runes_output import SolverRunesOutput
from utils import saveFromTextBoxToFile


class IoursUi:
    def __init__(self, master=None):
        # build ui
        self.root = ttk.Frame(master)
        self.root.configure(height='200', width='200')
        self.root.pack(expand='true', ipadx='0', ipady='0', padx='10', pady='10', side='top')

        self.tab_control = ttk.Notebook(self.root)
        self.tab_control.grid(column='0', row='0')

        self.RunesInputFrame = SolverRunesInput(self.tab_control)
        self.ShipInputFrame = ttk.Frame(self.tab_control)

        self.tab_control.add(self.RunesInputFrame.root, text='Runes Solver')
        self.tab_control.add(self.ShipInputFrame, text='Ship Arena Solver')

        self.OutputFrame = SolverRunesOutput(self.root)
        self.OutputFrame.root.grid(column='1', row='0')

        # Button Calculate
        self.button = ttk.Button(self.root, command=self.chooseCallback)
        self.button.configure(text='Calculate', )
        self.button.grid(column='0', columnspan='2', padx='5', pady='5', row='1')
        # Progress bar
        self.progress = ttk.Progressbar(self.root, mode='determinate', length=1200, maximum=110)
        self.progress.grid(column='0', row='2', columnspan='2')

        self.params_tk = {
            'progress': self.progress,
            'plot_frame': self.OutputFrame.PlotFrame,
        }

    def run(self):
        self.root.mainloop()

    def chooseCallback(self):
        # Save must be done here
        LoaderMaster().re()

        if self.tab_control.index("current") == 0:
            self.chooseCallbackPets()
        if self.tab_control.index("current") == 1:
            self.chooseCallbackShip()

    def chooseCallbackPets(self):
        params = {
            'pets': LoaderMaster().pets.pets,
            'bonus': LoaderMaster().pets.bonus,
            'runes': LoaderMaster().pets.runes,
            'rune1_rarity': int(self.RunesInputFrame.RunesFrame.spinbox_r1r.get()),
            'rune1_level': int(self.RunesInputFrame.RunesFrame.spinbox_r1l.get()),
            'rune2_rarity': int(self.RunesInputFrame.RunesFrame.spinbox_r2r.get()),
            'rune2_level': int(self.RunesInputFrame.RunesFrame.spinbox_r2l.get()),
            'opponent_level': int(self.RunesInputFrame.OpponentFrame.spinbox_op.get()),
            'arena': LoaderMaster().pets.runes.arena,
            'limit': int(self.RunesInputFrame.OpponentFrame.spinbox_limit.get())+1,
            'capped': self.RunesInputFrame.OpponentFrame.var_check.get(),
        }
        if self.RunesInputFrame.OpponentFrame.var_radio.get() == 0:
            call = CalculateCallback("PetsOneLevel")
        else:
            call = CalculateCallback("PetsContinuous")
        call.do(params, self.params_tk)

    def chooseCallbackShip(self):
        print(self.RunesInputFrame.OpponentFrame.var_radio.get())
        tkinter.messagebox.showinfo("", "Coming soon")

