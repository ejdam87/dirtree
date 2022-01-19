import tkinter as tk
from tkinter import filedialog
import dirtree

class Window:

    def __init__(self):

        self.root = tk.Tk()
        self.strtree = tk.StringVar()
        self.strtree.set("xx")
        self.box = tk.Text(self.root, width=100, height = 30)
        self.submit_button = tk.Button(self.root, text="Get dirtree!", command=self.eval)
        self.select_root_button = tk.Button(self.root, text="Select root", command=self.get_root)
        self.root_folder = None

        self.box.pack(expand=True)
        self.submit_button.pack(expand=True)
        self.select_root_button.pack(expand=True)

    def get_root(self):
        self.root_folder = filedialog.askdirectory()

    def eval(self):

        tree = str(dirtree.load_dirtree(self.root_folder))
        self.box.insert("end", tree)


window = Window()
window.root.mainloop()