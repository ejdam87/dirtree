import tkinter as tk
from tkinter import filedialog
import dirtree

class Window:

    def __init__(self) -> None:

        self.root = tk.Tk()
        self.strtree = tk.StringVar()
        self.selected= tk.StringVar()

        # --- Widgets
        self.box = tk.Text(self.root, width=100, height = 30)
        self.submit_button = tk.Button(self.root, text="Get dirtree!", command=self.eval)
        self.select_root_button = tk.Button(self.root, text="Select root", command=self.get_root)
        self.selected_root_label = tk.Label(self.root, textvariable=self.selected)
        # ---

        self.root_folder = None

        self.box.pack(expand=True)
        self.submit_button.pack(expand=True)
        self.select_root_button.pack(expand=True)
        self.selected_root_label.pack(expand=True)

    def get_root(self) -> None:

        self.root_folder = filedialog.askdirectory()
        self.selected.set(self.root_folder)

    def eval(self) -> None:

        tree = str(dirtree.load_dirtree(self.root_folder))
        self.box.insert("end", tree)


window = Window()
window.root.mainloop()
