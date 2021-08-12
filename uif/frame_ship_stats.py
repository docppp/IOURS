import tkinter.ttk as ttk


class FrameShipStats:
    def __init__(self, master):
        self.root = ttk.Labelframe(master)
        self.root.configure(height='200', text='Ship Data Input', width='100')

        self.spinbox_virt = ttk.Spinbox(self.root)
        self.spinbox_virt.configure(from_='0', to='999', width='4')
        self.spinbox_virt.grid(column='1', row='0', sticky='w')

        self.spinbox_orbs = ttk.Spinbox(self.root)
        self.spinbox_orbs.configure(from_='0', to='7', width='4')
        self.spinbox_orbs.grid(column='1', row='1', sticky='w')

        self.spinbox_orbl = ttk.Spinbox(self.root)
        self.spinbox_orbl.configure(from_='0', to='99', width='4')
        self.spinbox_orbl.grid(column='1', row='2', sticky='w')

        self.spinbox_lege = ttk.Spinbox(self.root)
        self.spinbox_lege.configure(from_='0', to='50', width='4')
        self.spinbox_lege.grid(column='1', row='3', sticky='w')

        self.spinbox_ascd = ttk.Spinbox(self.root)
        self.spinbox_ascd.configure(from_='0', to='10', width='4')
        self.spinbox_ascd.grid(column='1', row='4', sticky='w')

        self.spinbox_asch = ttk.Spinbox(self.root)
        self.spinbox_asch.configure(from_='0', to='10', width='4')
        self.spinbox_asch.grid(column='1', row='5', sticky='w')

        self.spinbox_trph = ttk.Spinbox(self.root)
        self.spinbox_trph.configure(from_='0', to='100', width='4')
        self.spinbox_trph.grid(column='1', row='6', sticky='w')

        self.spinbox_trpd = ttk.Spinbox(self.root)
        self.spinbox_trpd.configure(from_='0', to='100', width='4')
        self.spinbox_trpd.grid(column='1', row='7', sticky='w')

        # Labels
        texts = ['Virtue Level', 'Ship Orb Star', 'Ship Orb Level', 'Legendary Dmg',
                 'Asc Damage', 'Asc Health', 'Trophy Health', 'Trophy Damage']

        for i, text in enumerate(texts):
            label = ttk.Label(self.root)
            label.configure(text=text)
            label.grid(column='0', padx='10', row=str(i), sticky='w')
            label.columnconfigure('0', pad='10')
