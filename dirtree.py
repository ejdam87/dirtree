from typing import List
import os
import shutil
from directory import Directory
import shutil


def create_dirtree(path: str, tree: Directory) -> None:

    new_path = path + os.path.sep + tree.name

    if not os.path.isdir(new_path):
        os.mkdir(new_path)

    if tree.dirs == []:
        return

    for subdir in tree.dirs:
        create_dirtree(new_path, subdir)


def load_dirtree(path: str) -> Directory:

    files = os.listdir(path)

    if files == []:

        folder = path.split(os.path.sep)[-1]
        return Directory(folder, [])

    children = []
    for folder in files:

        if os.path.isdir(path + os.path.sep + folder):
            children.append(load_dirtree(path + os.path.sep + folder))

    root = path.split(os.path.sep)[-1]
    return Directory(root, children)


def parse_string_tree(string: str) -> Directory:

    indent_chars = {"─","└", "│", "├"}
    normalized = string

    for ichar in indent_chars:
        normalized = normalized.replace(ichar, " ")

    rows = normalized.split("\n")
    root_name = rows[0]

    return parse_rec(root_name, rows[1:], 0, max_level(rows))


def parse_rec(name: str, 
              rows_left: List[str],
              level: int,
              max_level: int) -> Directory:
    
    if level == max_level:
        return Directory(name, [])

    subdirs = []
    for i, child in enumerate(rows_left):

        indent = len(child) - len(child.lstrip())
        new = child.lstrip()
        new_level = (indent - 1) // 3 + 1

        if new_level <= level:  # We reached end of subdirs
            break

        if new_level == level + 1:  # Found subdir
            subdirs.append(parse_rec(new, rows_left[i + 1:], level + 1, max_level))

    return Directory(name, subdirs)


def max_level(rows: List[str]) -> int:

    current = 0
    for row in rows:
        
        indent = len(row) - len(row.lstrip())
        level = (indent - 1) // 3 + 1
        if level > current:
            current = level

    return current
