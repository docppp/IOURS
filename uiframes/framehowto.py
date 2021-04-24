import tkinter.ttk as ttk


class FrameHowTo:
    def __init__(self, master):
        self.labelframe = ttk.Labelframe(master)
        self.labelframe.configure(height='200', text='How to use it?', width='200')
        self.labelframe.grid(column='1', row='0', sticky='nw')
        self.labelframe.rowconfigure('0', weight='1')
        self.labelframe.columnconfigure('1', minsize='150', pad='0', weight='1')

        self.label = ttk.Label(self.labelframe)
        self.label.pack(padx='10', side='top')
        self.label.configure(justify='left', text='After pasting all data, choose opponent level to fight with.'
                                                  ' Program calculates combination of runes which requires least'
                                                  ' heals to win. Choose continuous mode to see which runes are'
                                                  ' better in the long run (limited to 50 lvl). Your pet input data'
                                                  ' is stored in iou.txt file.', wraplength='220')
