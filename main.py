import tkinter.messagebox
from utils import fillTextBoxAtStartup
from ui import IoursUi


if __name__ == '__main__':
    import tkinter as tk
    root = tk.Tk()
    app = IoursUi(root)
    if not fillTextBoxAtStartup(app.text1, app.text2, app.entry1):
        # TODO
        # Textbox should be cleared here, but
        # they are disabled after removing content
        tkinter.messagebox.showinfo("No data found", "Wrong or no data found in iou.txt "
                                                     "If run this app for the first time, then it is ok.")
    app.run()

