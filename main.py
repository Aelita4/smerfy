import tkinter as tk
import os.path

from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile


def saveFileAs():

    inp = text_box.get(1.0, "end-1c")

    fileName = "New File"

    files = [('All Files', '*.*'),
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
    file = asksaveasfile(filetypes = files, defaultextension = ".txt", initialfile= fileName)
    file.write(inp)

def saveFile():
    print ("Zapisane")

def openFile():

    filename = askopenfile(filetypes=[("Text files","*.txt")])
    txt = filename.read()
    text_box.insert(1.0, txt)

window = tk.Tk()
#window.geometry()
btn1 = tk.Button(
    text="Save",
    width=25,
    bg="gray",
    fg="white",
    command= saveFile,
)
btn2 = tk.Button(
    text="Save as",
    width=25,
    bg="gray",
    fg="white",
    command= saveFileAs,
)
btn3 = tk.Button(
    text="Open",
    width=25,
    bg="gray",
    fg="white",
    command= openFile,
)
btn4 = tk.Button(
    text="Copy",
    width=25,
    bg="gray",
    fg="white",
)
btn5 = tk.Button(
    text="Paste",
    width=25,
    bg="gray",
    fg="white",
)
text_box = tk.Text(width=115)

btn1.grid(row=0, column=0, sticky="we")
btn2.grid(row=0, column=1, sticky="we")
btn3.grid(row=0, column=2, sticky="we")
btn4.grid(row=0, column=3, sticky="we")
btn5.grid(row=0, column=4, sticky="we")


text_box.grid(columnspan=6)

window.title("Notatnik")
window.mainloop()
