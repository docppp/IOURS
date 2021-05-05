import tkinter.ttk as ttk


class FrameHowTo:
    def __init__(self, master):
        self.labelframe = ttk.Labelframe(master)
        self.labelframe.configure(height='100', text='How to use it?', width='430')
        self.labelframe.grid(column='0', row='0', sticky='nw', columnspan='2')
        self.labelframe.rowconfigure('0', weight='1')
        self.labelframe.columnconfigure('1', minsize='150', pad='0', weight='1')

        self.label = ttk.Label(self.labelframe)
        self.label.pack(padx='10', side='top')
        self.label.configure(justify='left', text='After pasting all data, choose opponent level to fight with.'
                                                  ' Program calculates combination of runes which requires least'
                                                  ' heals to win. Choose "Continuous" mode to see which runes are'
                                                  ' better in the long run - spinbox "Limit" defines the range'
                                                  ' of the calculated levels (large ranges can took long time to'
                                                  ' calculate, be carreful). Select "Cap Heals" to cap heals usage'
                                                  ' - you cannot win if used heals are above 250. Your pet input'
                                                  ' and runes data are stored in iou.txt file. This is v1.1 IOURS.',
                             wraplength='643')
