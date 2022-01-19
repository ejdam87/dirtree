import tkinter as tk
from tkinter import filedialog
import file_lookup
from typing import Optional
import os


def lookup(path: str, needle: str) -> Optional[str]:
    """
    Returns path to file if found else None
    """
    
    files = os.listdir(path)
    if needle in files:
        return path

    for file in files:
        if os.path.isdir(file):
            found = lookup(path + os.path.sep + file, needle)
            if found:
                return found

    return None


class Window:

    def __init__(self) -> None:

        self.root = tk.Tk()
        self.selected= tk.StringVar()
        self.result = tk.StringVar()

        # --- Widgets
        self.entry = tk.Entry(self.root, width=30)
        self.submit_button = tk.Button(self.root, text="Find file!", command=self.search)
        self.select_root_button = tk.Button(self.root, text="Select finding-root", command=self.get_root)
        self.selected_root_label = tk.Label(self.root, textvariable=self.selected)
        self.result_label = tk.Label(self.root, textvariable=self.result)
        # ---

        self.root_folder = None

        self.entry.pack(expand=True)
        self.submit_button.pack(expand=True)
        self.select_root_button.pack(expand=True)
        self.selected_root_label.pack(expand=True)
        self.result_label.pack(expand = True)

    def get_root(self) -> None:

        self.root_folder = filedialog.askdirectory()
        self.selected.set(self.root_folder)

    def search(self) -> None:

        needle = self.entry.get()
        val = lookup(self.root_folder, needle)
        self.result.set(val)



window = Window()
window.root.mainloop()
