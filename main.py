from ctypes import CDLL
from multiprocessing import freeze_support

from utils import fillTextBoxAtStartup
from ui import IoursUi
import tkinter as tk

if __name__ == '__main__':
    freeze_support()
    dll_found = True
    try:
        dll = CDLL('./fight.dll')
    except FileNotFoundError:
        dll_found = False
    root = tk.Tk()
    root.title('IOURS - IOU Runes Solver')
    app = IoursUi(root)
    if not fillTextBoxAtStartup(app.Petframe.text1, app.Petframe.text2, app.Petframe.entry1,
                                app.Runesframe, app.OpponentFrame):
        app.Petframe.text1.delete('0.0', 'end')
        app.Petframe.text2.delete('0.0', 'end')
        app.Petframe.entry1.delete('0', 'end')
        app.Petframe.text1.insert('0.0', 'Wrong or no data\nfound in iou.txt\n'
                                         'Its ok if you run\nthis app for the first time.')
    if not dll_found:
        app.Petframe.text2.delete('0.0', 'end')
        app.Petframe.text2.insert('0.0', 'Cannot find fight.dll\nProgram will not work.')
        app.OpponentFrame.button.configure(state='disabled')

    app.run()
