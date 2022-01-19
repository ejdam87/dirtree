from typing import List
import os
import shutil


# V této úloze budete pracovat s reprezentací adresářové struktury.
# Každý adresář má své jméno ‹name› a seznam podadresářů ‹dirs›.

class Directory:
    def __init__(self, name: str, dirs: List['Directory']):
        self.name = name
        self.dirs = dirs

    def __repr__(self) -> str:
        """
        Method to get text-representation of tree
        """

        out = []
        self.draw_levels(self, 0, "", "", out)

        return "\n".join(out)

    def draw_levels(self,
                    directory: "Directory",
                    level: int,
                    branching: str,
                    previous: str,
                    output: List[str]) -> None:

        """
        Help-func for text representation of tree
        """

        content = directory.name

        if level != 0:
            spacing = "─ "
        else:
            spacing = ""

        ln = previous + branching + spacing + content

        # Console output
        # print(ln)

        output.append(ln)


        vertical = "│" if branching == "├" else ""

        if vertical == "":
            if level != 0:
                padding = 3 * " "
            else:
                padding = ""
        else:
            padding = 2 * " "

        previous += vertical + padding

        for i in range(len(directory.dirs)):

            # If we are starting new branch
            if i == 0:
                branching = "├"

            # If we finish current branch
            if i == len(directory.dirs) - 1:
                branching = "└"

            # Goin' deeper
            self.draw_levels(directory.dirs[i],
                level + 1, branching, previous, output)


def create_dirtree(path: str, tree: Directory) -> None:

    os.mkdir(path + os.path.sep + tree.name)

    if tree.dirs == []:
        return

    for subdir in tree.dirs:
        create_dirtree(path + os.path.sep + tree.name, subdir)


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

        indent = space_from_left(child)
        new = child.lstrip()
        new_level = (indent - 1) // 3 + 1

        if new_level == level + 1:
            subdirs.append(parse_rec(new, rows_left[i + 1:], level + 1, max_level))

    return Directory(name, subdirs)


def max_level(rows: List[str]) -> int:

    current = 0
    for row in rows:
        
        indent = space_from_left(row)
        level = (indent - 1) // 3 + 1
        if level > current:
            current = level

    return current


def space_from_left(row: str) -> int:

    total = 0

    for char in row:
        if char != " ":
            break

        total += 1

    return total

