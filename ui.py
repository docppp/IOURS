from tkinter import *
import tkinter.ttk as ttk
import tkinter as tk
import tkinter.messagebox

from load import loadThings
from ioumath import getBestRunes
from utils import saveFromTextBoxToFile


class IoursUi:
    def __init__(self, master=None):
        # build ui
        self.root = ttk.Frame(master)
        self.Inputframe = ttk.Frame(self.root)

        #
        # PET FRAME
        #

        self.Petframe = ttk.Labelframe(self.Inputframe)
        self.label1 = ttk.Label(self.Petframe)
        self.label1.configure(text="""C23:D31 from PetCombat
(hidden sheet) e.g.:""")
        self.label1.grid(column='0', row='0', sticky='ne')
        self.text1 = tk.Text(self.Petframe)
        self.text1.configure(height='9', width='30')
        self.text1.grid(column='1', padx='10', pady='0', row='0', rowspan='2', sticky='n')
        self.label2 = ttk.Label(self.Petframe)
        self.label2.configure(text="""AP Arena Stats	
Pet 1	Pet 2
4,385,976,371	4,385,976,371
73,837	73,837
5.10%	Heals
992.00%	39.00%
35.60%	Favor
0.00%	7.40%
9.75%	""")
        self.label2.grid(column='0', row='1', sticky='ne')
        self.text2 = tk.Text(self.Petframe)
        self.text2.configure(height='7', setgrid='true', width='30')
        self.text2.grid(column='1', padx='10', pady='0', row='2', rowspan='2', sticky='n')
        self.label3 = ttk.Label(self.Petframe)
        self.label3.configure(text="""N26:O32 from Runes
e.g.:""")
        self.label3.grid(column='0', row='2', sticky='ne')
        self.entry1 = ttk.Entry(self.Petframe)
        self.entry1.configure(width='40')
        self.entry1.grid(column='1', padx='10', pady='10', row='4', sticky='w')
        self.label5 = ttk.Label(self.Petframe)
        self.label5.configure(text="""Adrenaline Rush	0.00%
Anger Issues	0.00%
Favor	7.40%
Frenzy	74.00%
Poisonous	9.75%
Premeditated	0.00%
Regen	26.00%""")
        self.label5.grid(column='0', row='3', sticky='ne')
        self.label6 = ttk.Label(self.Petframe)
        self.label6.configure(text='Coverage e.g.: "Coverage 84.00%"')
        self.label6.grid(column='0', row='4', sticky='e')
        self.Petframe.configure(height='200', text='Pet Data Input', width='200')
        self.Petframe.grid(column='0', row='0', rowspan='3')
        self.Petframe.rowconfigure('0', weight='1')
        self.Petframe.columnconfigure('0', weight='1')

        #
        # RUNES FRAME
        #

        self.Runesframe = ttk.Labelframe(self.Inputframe)
        self.label7 = ttk.Label(self.Runesframe)
        self.label7.configure(text='Rune 1 Rarity')
        self.label7.grid(column='0', padx='5', pady='5', row='0')
        self.label7.columnconfigure('0', minsize='0', pad='0')
        self.spinbox_r1r = ttk.Spinbox(self.Runesframe, from_=0, to=99)
        self.spinbox_r1r.configure(increment='1', justify='left', width='5')
        self.spinbox_r1r.grid(column='1', row='0', sticky='w')
        self.spinbox_r1r.columnconfigure('1', minsize='0', pad='20')
        self.spinbox_r1r.insert('0', '1')

        self.label8 = ttk.Label(self.Runesframe)
        self.label8.configure(text='Rune 1 Level')
        self.label8.grid(column='0', padx='5', pady='5', row='1')
        self.label8.columnconfigure('0', minsize='0', pad='0')
        self.spinbox_r1l = ttk.Spinbox(self.Runesframe, from_=0, to=10)
        self.spinbox_r1l.configure(increment='1', width='5')
        self.spinbox_r1l.grid(column='1', row='1', sticky='w')
        self.spinbox_r1l.columnconfigure('1', minsize='0', pad='20')
        self.spinbox_r1l.insert('0', '1')

        self.label9 = ttk.Label(self.Runesframe)
        self.label9.configure(text='Rune 2 Rarity')
        self.label9.grid(column='0', padx='5', pady='5', row='2')
        self.label9.columnconfigure('0', minsize='0', pad='0')
        self.spinbox_r2r = ttk.Spinbox(self.Runesframe, from_=0, to=99)
        self.spinbox_r2r.configure(increment='1', width='5')
        self.spinbox_r2r.grid(column='1', row='2', sticky='w')
        self.spinbox_r2r.columnconfigure('1', minsize='0', pad='20')
        self.spinbox_r2r.insert('0', '1')

        self.label10 = ttk.Label(self.Runesframe)
        self.label10.configure(text='Rune 2 Level')
        self.label10.grid(column='0', padx='5', pady='5', row='3')
        self.label10.columnconfigure('0', minsize='0', pad='0')
        self.spinbox_r2l = ttk.Spinbox(self.Runesframe, from_=0, to=10)
        self.spinbox_r2l.configure(increment='1', width='5')
        self.spinbox_r2l.grid(column='1', row='3', sticky='w')
        self.spinbox_r2l.columnconfigure('1', minsize='0', pad='20')
        self.spinbox_r2l.insert('0', '1')

        self.Runesframe.configure(height='200', text='Runes Data Input', width='200')
        self.Runesframe.grid(column='1', row='1', sticky='sw')
        self.Runesframe.rowconfigure('1', minsize='0', weight='1')
        self.Runesframe.columnconfigure('1', minsize='150', pad='0', weight='1')

        #
        # OPPONENT FRAME
        #
        self.var_opponent_button = IntVar()

        self.Opponentframe = ttk.Labelframe(self.Inputframe)
        self.label12 = ttk.Label(self.Opponentframe)
        self.label12.configure(text='Opponent Level')
        self.label12.grid(column='0', padx='10', pady='10', row='0')
        self.spinbox_op = ttk.Spinbox(self.Opponentframe, from_=1, to=999)
        self.spinbox_op.configure(increment='1', width='5')
        self.spinbox_op.grid(column='1', row='0')
        self.spinbox_op.columnconfigure('1', pad='20')
        self.spinbox_op.insert('0', '1')

        self.radiobutton1 = ttk.Radiobutton(self.Opponentframe, variable=self.var_opponent_button, value=0)
        self.radiobutton1.configure(text='One level')
        self.radiobutton1.grid(column='0', row='1')
        self.radiobutton2 = ttk.Radiobutton(self.Opponentframe, variable=self.var_opponent_button, value=1)
        self.radiobutton2.configure(state='normal', text='Continuous')
        self.radiobutton2.grid(column='1', row='1')

        self.button1 = ttk.Button(self.Opponentframe, command=self.buttonCallback)
        self.button1.configure(text='Calculate')
        self.button1.grid(column='0', columnspan='2', padx='5', pady='5', row='2')
        self.Opponentframe.configure(height='200', text='Opponent Data Input', width='200')
        self.Opponentframe.grid(column='1', row='2', sticky='sw')
        self.Opponentframe.rowconfigure('2', weight='1')
        self.Opponentframe.columnconfigure('1', minsize='125', pad='0', weight='1')

        #
        # HOW TO FRAME
        #

        self.labelframe4 = ttk.Labelframe(self.Inputframe)
        self.label13 = ttk.Label(self.labelframe4)
        self.label13.configure(justify='left', text='After pasting all data, choose opponent level to fight with.'
                                                    ' Program calculates combination of runes which requires least'
                                                    ' heals to win. Choose continuous mode to see which runes are'
                                                    ' better in the long run (limited to 50 lvl).', wraplength='220')
        self.label13.pack(padx='10', side='top')
        self.labelframe4.configure(height='200', text='How to use it?', width='200')
        self.labelframe4.grid(column='1', row='0', sticky='nw')
        self.labelframe4.rowconfigure('0', weight='1')
        self.labelframe4.columnconfigure('1', minsize='150', pad='0', weight='1')
        self.Inputframe.configure(height='200', width='200')
        self.Inputframe.pack(expand='true', side='top')
        self.frame7 = ttk.Frame(self.root)
        self.canvas1 = tk.Canvas(self.frame7)
        self.canvas1.pack(side='top')
        self.frame7.configure(height='200', width='200')
        self.frame7.pack(side='top')
        self.root.configure(height='200', width='200')
        self.root.pack(expand='true', ipadx='10', ipady='10', padx='10', pady='10', side='top')

        # Main widget
        self.mainwindow = self.root

    def run(self):
        self.mainwindow.mainloop()

    def buttonCallback(self):
        print(self.var_opponent_button.get())
        if self.var_opponent_button.get() == 0:
            self.buttonOneLevelClicked()
        if self.var_opponent_button.get() == '1':
            self.buttonOneLevelClicked()

    def buttonOneLevelClicked(self):
        if not saveFromTextBoxToFile(self.text1, self.text2, self.entry1):
            tkinter.messagebox.showinfo("Error", "There were some error during saving data to iou.txt")
            return False

        try:
            pet1, pet2, bonus, runes = loadThings()
        except Exception:
            tkinter.messagebox.showinfo("Error", "There were some error during data parsing")
            return False

        rune1_rarity = int(self.spinbox_r1r.get())
        rune1_level = int(self.spinbox_r1l.get())
        rune2_rarity = int(self.spinbox_r2r.get())
        rune2_level = int(self.spinbox_r2l.get())
        opponent_level = int(self.spinbox_op.get())

        try:
            ans = getBestRunes(pet1, pet2, bonus, rune1_rarity, rune1_level, rune2_rarity, rune2_level, opponent_level)
            tkinter.messagebox.showinfo("Best Rune", ans)
        except Exception:
            tkinter.messagebox.showinfo("Error", "There were some error during calculations")
            return False

        return True




