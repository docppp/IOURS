import tkinter.ttk as ttk


class FrameRunes:
    def __init__(self, master):
        self.Framerunes = ttk.Labelframe(master)
        self.Framerunes.configure(height='200', text='Runes Data Input', width='210')
        self.Framerunes.rowconfigure('1', minsize='0', weight='1')
        self.Framerunes.columnconfigure('1', minsize='100', pad='0', weight='1')

        # Spinbox
        self.spinbox_r1r = ttk.Spinbox(self.Framerunes, from_=0, to=99)
        self.spinbox_r1r.configure(increment='1', justify='left', width='5')
        self.spinbox_r1r.grid(column='1', row='0', sticky='w')
        self.spinbox_r1r.columnconfigure('1', minsize='0', pad='20')

        self.spinbox_r1l = ttk.Spinbox(self.Framerunes, from_=0, to=10)
        self.spinbox_r1l.configure(increment='1', width='5')
        self.spinbox_r1l.grid(column='1', row='1', sticky='w')
        self.spinbox_r1l.columnconfigure('1', minsize='0', pad='20')

        self.spinbox_r2r = ttk.Spinbox(self.Framerunes, from_=0, to=99)
        self.spinbox_r2r.configure(increment='1', width='5')
        self.spinbox_r2r.grid(column='1', row='2', sticky='w')
        self.spinbox_r2r.columnconfigure('1', minsize='0', pad='20')

        self.spinbox_r2l = ttk.Spinbox(self.Framerunes, from_=0, to=10)
        self.spinbox_r2l.configure(increment='1', width='5')
        self.spinbox_r2l.grid(column='1', row='3', sticky='w')
        self.spinbox_r2l.columnconfigure('1', minsize='0', pad='20')

        # Labels
        self.label1 = ttk.Label(self.Framerunes)
        self.label1.configure(text='Rune 1 Rarity')
        self.label1.grid(column='0', padx='18', pady='5', row='0')
        self.label1.columnconfigure('0', minsize='0', pad='0')

        self.label2 = ttk.Label(self.Framerunes)
        self.label2.configure(text='Rune 1 Level')
        self.label2.grid(column='0', padx='5', pady='5', row='1')
        self.label2.columnconfigure('0', minsize='0', pad='0')

        self.label3 = ttk.Label(self.Framerunes)
        self.label3.configure(text='Rune 2 Rarity')
        self.label3.grid(column='0', padx='5', pady='5', row='2')
        self.label3.columnconfigure('0', minsize='0', pad='0')

        self.label4 = ttk.Label(self.Framerunes)
        self.label4.configure(text='Rune 2 Level')
        self.label4.grid(column='0', padx='5', pady='5', row='3')
        self.label4.columnconfigure('0', minsize='0', pad='0')
