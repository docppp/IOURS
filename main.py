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
    root.title('IOUR Solvers')
    app = IoursUi(root)
    LoaderMaster().loadFile()
    if not fillTextBoxAtStartup(app.RunesInputFrame.PetFrame.text1, app.RunesInputFrame.PetFrame.text2, app.RunesInputFrame.PetFrame.entry1,
                                app.RunesInputFrame.RunesFrame, app.RunesInputFrame.OpponentFrame):
        app.RunesInputFrame.PetFrame.text1.delete('0.0', 'end')
        app.RunesInputFrame.PetFrame.text2.delete('0.0', 'end')
        app.RunesInputFrame.PetFrame.entry1.delete('0', 'end')
        app.RunesInputFrame.PetFrame.text1.insert('0.0', 'Wrong or no data\nfound in iou.txt\n'
                                         'Its ok if you run\nthis app for the first time.')
    if not dll_found:
        app.RunesInputFrame.PetFrame.text2.delete('0.0', 'end')
        app.RunesInputFrame.Petframe.text2.insert('0.0', 'Cannot find fight.dll\nProgram will not work.')
        app.button.configure(state='disabled')

    app.run()
