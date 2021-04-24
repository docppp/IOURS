import tkinter.ttk as ttk
from tkinter import IntVar


class FrameOpponent:
    def __init__(self, master, buttoncallback):
        self.var_radio = IntVar()
        self.Frameopponent = ttk.Labelframe(master)
        self.Frameopponent.configure(height='200', text='Opponent Data Input', width='200')
        self.Frameopponent.grid(column='1', row='2', sticky='sw')
        self.Frameopponent.rowconfigure('2', weight='1')
        self.Frameopponent.columnconfigure('1', minsize='125', pad='0', weight='1')

        # Opponent level spinbox
        self.spinbox_op = ttk.Spinbox(self.Frameopponent, from_=1, to=999)
        self.spinbox_op.configure(increment='1', width='5')
        self.spinbox_op.grid(column='1', row='0')
        self.spinbox_op.columnconfigure('1', pad='20')
        self.spinbox_op.insert('0', '1')

        # Radiobutton - One level or Continuous
        self.radiobutton1 = ttk.Radiobutton(self.Frameopponent, variable=self.var_radio, value=0)
        self.radiobutton1.configure(text='One level')
        self.radiobutton1.grid(column='0', row='1')
        self.radiobutton2 = ttk.Radiobutton(self.Frameopponent, variable=self.var_radio, value=1)
        self.radiobutton2.configure(state='normal', text='Continuous')
        self.radiobutton2.grid(column='1', row='1')

        # Button Calculate
        self.button = ttk.Button(self.Frameopponent, command=buttoncallback)
        self.button.configure(text='Calculate')
        self.button.grid(column='0', columnspan='2', padx='5', pady='5', row='2')

        # Labels
        self.label = ttk.Label(self.Frameopponent)
        self.label.configure(text='Opponent Level')
        self.label.grid(column='0', padx='10', pady='10', row='0')





