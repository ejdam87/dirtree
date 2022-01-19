from typing import List

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
