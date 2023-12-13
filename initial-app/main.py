import tkinter as tk
from tkinter import ttk


def greet():
    print("Example project")


root = tk.Tk()
ttk.Label(root, text="This is an example app", padding=(30, 10)).pack()
greet_button = ttk.Button(text="greet", command=greet, padding=(20, 10))
greet_button.pack(side="left", fill="x", expand=True)

quit_button = ttk.Button(text="quit", command=root.destroy, padding=(20, 10))
quit_button.pack(side="left", fill="x")

root.mainloop()
