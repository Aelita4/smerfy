import tkinter as tk
import os.path

from tkinter.filedialog import asksaveasfile

from tOpen import open_file

def save_file():

    inp = text_box.get(1.0, "end-1c")

    fileName = "New File"

    files = [('All Files', '*.*'),
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]
    file = asksaveasfile(filetypes = files, defaultextension = ".txt", initialfile= fileName)
    file.write(inp)

    # fileNr = 0
    # inp = text_box.get(1.0, "end-1c")
    # file_name = e.get()
    #
    # if file_name == "":
    #     file_name = "New File"
    #
    # if os.path.isfile('Text_Files/' + file_name):
    #     fileNr += 1
    #     file_name += " " + str(fileNr)
    #
    # text_file = open("Text_Files/" + file_name, "w")
    # n = text_file.write(inp)
    # print("Plik został zapisany jako *" + file_name + "* | w " + "*Text_Files*"  )

window = tk.Tk()
#window.geometry()
btn1 = tk.Button(
    text="Zapisz",
    width=25,
    bg="gray",
    fg="white",
    command= save_file,
)
btn2 = tk.Button(
    text="Otwórz",
    width=25,
    bg="gray",
    fg="white",
    command= open_file,
)
btn3 = tk.Button(
    text="kopiuj",
    width=25,
    bg="gray",
    fg="white",
)
btn4 = tk.Button(
    text="Wklej",
    width=25,
    bg="gray",
    fg="white",
)
text_box = tk.Text(width=92)

btn1.grid(row=0, column=0, sticky="we")
btn2.grid(row=0, column=1, sticky="we")
btn3.grid(row=0, column=2, sticky="we")
btn4.grid(row=0, column=3, sticky="we")


text_box.grid(columnspan=6)

window.title("Notatnik")
window.mainloop()
