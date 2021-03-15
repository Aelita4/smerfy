import tkinter as tk


from tOpen import open_file
from tSave import save_file


btn1 = tk.Button(
    text="Zapisz",
    width=25,
    height=1,
    bg="gray",
    fg="white",
    command= save_file,

)
btn2 = tk.Button(
    text="Otwórz",
    width=25,
    height=1,
    bg="gray",
    fg="white",
    command= open_file,
)
btn3 = tk.Button(
    text="kopiuj",
    width=25,
    height=1,
    bg="gray",
    fg="white",
)
btn4 = tk.Button(
    text="Wklej",
    width=25,
    height=1,
    bg="gray",
    fg="white",
)

e = tk.Entry(
    width= 15,
)

btn1.grid(row=0, column=0, sticky="we")
e.grid(row=0, column=1, sticky="we")
btn2.grid(row=0, column=2, sticky="we")
btn3.grid(row=0, column=3, sticky="we")
btn4.grid(row=0, column=4, sticky="we")

text_box = tk.Text(width=115)
text_box.grid(columnspan=6)
