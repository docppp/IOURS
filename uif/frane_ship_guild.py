import tkinter.ttk as ttk
import tkinter as tk


class FrameShipGuild:
    def __init__(self, master):
        self.root = ttk.Labelframe(master)
        self.root.configure(height='200', text='Guild Bonus Input', width='100', padding='5')

        self.label = ttk.Label(self.root)
        self.label.configure(text="""B4:C5 from Arena e.g.:
Space Academy   740.90 %
AI Guild Passive    114.80 %""")
        self.label.pack(side='left')

        self.guild_box = tk.Text(self.root)
        self.guild_box.configure(height='2', width='29')
        self.guild_box.pack(side='right')
