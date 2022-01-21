import tkinter as tk
from tkinter import filedialog, messagebox
import dirtree
import os


class Window:

    def __init__(self) -> None:

        self.root = tk.Tk()
        self.strtree = tk.StringVar()
        self.selected= tk.StringVar()

        # --- Widgets
        self.box = tk.Text(self.root, width=100, height = 30)
        self.select_root_button = tk.Button(self.root, text="Select root", command=self.get_root)
        self.create_button = tk.Button(self.root, text="Create dirtree", command=self.create)
        self.selected_root_label = tk.Label(self.root, textvariable=self.selected)
        # ---

        self.root_folder = None

        # --- Displayin' widgets
        self.box.pack(padx=20, pady=20, expand=True)
        self.select_root_button.pack(expand=True)
        self.create_button.pack(expand=True)
        self.selected_root_label.pack(expand=True)

    def get_root(self) -> None:

        self.root_folder = filedialog.askdirectory()
        self.selected.set(self.root_folder)
        self.eval()

    def eval(self) -> None:

        tree = str(dirtree.load_dirtree(self.root_folder))
        self.box.delete("1.0", "end-1c")
        self.box.insert("end", tree)

    def create(self) -> None:

        # Bad levels (nested)
        new = self.box.get("1.0", "end-1c")
        new_dirtree = dirtree.parse_string_tree(new)
        new_dirtree.name = new_dirtree.name.split("/")[-1]  # Gettin' rid of absolute path
        path = "/".join(self.root_folder.split("/")[:-1])   # Starting level above

        dirtree.create_dirtree(path, new_dirtree)



tk.Tk().withdraw()  # Prevents from opening Tk with warning msg
messagebox.showwarning("Warning!", "This app works with OS and can be harmful or easy to miss-use!")


window = Window()
window.root.mainloop()
