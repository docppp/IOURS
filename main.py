from utils import fillTextBoxAtStartup
from ui import IoursUi
import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    root.title('IOURS - IOU Rune Solver')
    app = IoursUi(root)
    if not fillTextBoxAtStartup(app.Petframe.text1, app.Petframe.text2, app.Petframe.entry1):
        app.Petframe.text1.delete('0.0', 'end')
        app.Petframe.text2.delete('0.0', 'end')
        app.Petframe.entry1.delete('0', 'end')
        app.Petframe.text1.insert('0.0', 'Wrong or no data\nfound in iou.txt\n'
                                         'Its ok if you run\nthis app for the first time.')

    app.run()
