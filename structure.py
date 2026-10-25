import tkinter as tk
from tkinter import ttk
root=tk.Tk()
root.geometry("900x600")
root.configure(bg="blue")
l=tk.Label(root, text="Choose your favorite programming language.", bg="blue", fg="red", font=("Times", 24, "bold"))
l.place(relx=0.5, rely=0.3, anchor="center")
choices=["Python", "Java", "C", "C++", "Html"]
choose=ttk.Combobox(root, values=choices, state="readonly")
choose.place(relx=0.5, rely=0.4, anchor="center")
choose.current(0)
a=tk.Label(root, text="", bg="blue", fg="red", font=("Times", 20, "bold"))
a.place(relx=0.5, rely=0.5, anchor="center")
def i(e):
    o=choose.get()
    a.config(text=f"You selected, {o}")
choose.bind("<<ComboboxSelected>>", i)
root.mainloop()