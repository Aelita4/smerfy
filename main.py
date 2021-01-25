import tkinter as tk

window = tk.Tk()
text_box = tk.Text(width=100)
btn1 = tk.Button(
    text="Zapisz",
    width=25,
    height=1,
    bg="gray",
    fg="white",
)
btn2 = tk.Button(
    text="Otwórz",
    width=25,
    height=1,
    bg="gray",
    fg="white",
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

btn1.grid(row=0, column=0, sticky="we")
btn2.grid(row=0, column=1, sticky="we")
btn3.grid(row=0, column=2, sticky="we")
btn4.grid(row=0, column=3, sticky="we")

text_box.grid(columnspan=4)

window.title("Notatnik")
window.mainloop()
