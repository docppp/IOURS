from ctypes import CDLL
from multiprocessing import freeze_support

from utils import fillTextBoxAtStartup
from ui import IoursUi
import tkinter as tk
from ldr.loader_master import LoaderMaster

if __name__ == '__main__':
    freeze_support()
    dll_found = True
    try:
        dll = CDLL('./fight.dll')
    except FileNotFoundError:
        dll_found = False
    root = tk.Tk()
    root.title('IOUR Solvers v.1.2a')
    app = IoursUi(root)
    LoaderMaster().loadFile()
    if not fillTextBoxAtStartup(app.RunesInputFrame.PetFrame.combat_box,
                                app.RunesInputFrame.PetFrame.runes_box,
                                app.RunesInputFrame.PetFrame.converge_box,
                                app.RunesInputFrame.RunesFrame,
                                app.RunesInputFrame.OpponentFrame,
                                app.ShipInputFrame.FrameShipStats,
                                app.ShipInputFrame.FrameShipGuild.guild_box):
        app.RunesInputFrame.PetFrame.combat_box.delete('0.0', 'end')
        app.RunesInputFrame.PetFrame.runes_box.delete('0.0', 'end')
        app.RunesInputFrame.PetFrame.converge_box.delete('0', 'end')
        app.RunesInputFrame.PetFrame.text1.insert('0.0', 'Wrong or no data\nfound in iou.txt\n'
                                                         'Its ok if you run\nthis app for the first time.')
    if not dll_found:
        app.RunesInputFrame.PetFrame.runes_box.delete('0.0', 'end')
        app.RunesInputFrame.Petframe.runes_box.insert('0.0', 'Cannot find fight.dll\nProgram will not work.')
        app.button.configure(state='disabled')

    app.run()
