import tkinter.ttk as ttk
import tkinter.messagebox
from ldr.loader_master import LoaderMaster
from rns.ioumath import getBestRunes
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
        self.tab_control.add(self.ShipInputFrame, text='Ship Solver Soon')

        self.OutputFrame = SolverRunesOutput(self.root)
        self.OutputFrame.root.grid(column='1', row='0')

        # Button Calculate
        self.button = ttk.Button(self.root, command=self.chooseCallback)
        self.button.configure(text='Calculate', )
        self.button.grid(column='0', columnspan='2', padx='5', pady='5', row='1')
        # Progress bar
        self.progress = ttk.Progressbar(self.root, mode='determinate', length=1200, maximum=110)
        self.progress.grid(column='0', row='2', columnspan='2')

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
            'capped': self.RunesInputFrame.OpponentFrame.var_check.get(),
            'progress': self.progress,
        }
        if self.RunesInputFrame.OpponentFrame.var_radio.get() == 0:
            call = CalculateCallback("PetsOneLevel")
        else:
            call = CalculateCallback("PetsContinuous")
        call.do(params)

    def chooseCallbackShip(self):
        print(self.RunesInputFrame.OpponentFrame.var_radio.get())
        print("Coming soon")

    # TODO
    # Better error handling
    def buttonCallback(self):
        if not saveFromTextBoxToFile(self.Petframe.text1, self.Petframe.text2, self.Petframe.entry1,
                                     self.Runesframe, self.OpponentFrame):
            tkinter.messagebox.showinfo("Error", "There were some error during saving data to iou.txt")
            return False

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
