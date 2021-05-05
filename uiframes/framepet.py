import tkinter.ttk as ttk
import tkinter as tk


class FramePet:
    def __init__(self, master):
        self.Framepet = ttk.Labelframe(master)
        self.Framepet.configure(height='200', text='Pet Data Input', width='200')
        self.Framepet.grid(column='0', row='0', rowspan='3')
        self.Framepet.rowconfigure('0', weight='1')
        self.Framepet.columnconfigure('0', weight='1')

        # PetCombat Input
        self.text1 = tk.Text(self.Framepet)
        self.text1.configure(height='9', width='30')
        self.text1.grid(column='1', padx='10', pady='0', row='0', rowspan='2', sticky='n')

        # Runes Input
        self.text2 = tk.Text(self.Framepet)
        self.text2.configure(height='7', setgrid='true', width='30')
        self.text2.grid(column='1', padx='10', pady='0', row='2', rowspan='2', sticky='n')

        # Converge Input
        self.entry1 = ttk.Entry(self.Framepet)
        self.entry1.configure(width='40')
        self.entry1.grid(column='1', padx='10', pady='10', row='4', sticky='w')

        # Labels
        self.label1 = ttk.Label(self.Framepet)
        self.label1.configure(text="""C23:D31 from PetCombat
(hidden sheet) e.g.:""")
        self.label1.grid(column='0', row='0', sticky='ne')

        self.label2 = ttk.Label(self.Framepet)
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

        self.label3 = ttk.Label(self.Framepet)
        self.label3.configure(text="""N26:O32 from Runes
        e.g.:""")
        self.label3.grid(column='0', row='2', sticky='ne')

        self.label4 = ttk.Label(self.Framepet)
        self.label4.configure(text="""Adrenaline Rush	0.00%
Anger Issues	0.00%
Favor	7.40%
Frenzy	74.00%
Poisonous	9.75%
Premeditated	0.00%
Regen	26.00%""")
        self.label4.grid(column='0', row='3', sticky='ne')

        self.label5 = ttk.Label(self.Framepet)
        self.label5.configure(text='Coverage e.g.: "Coverage 84.00%"')
        self.label5.grid(column='0', row='4', sticky='e')