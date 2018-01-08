from entities import *
from position import *
import os

class Maze:

    def __init__(self, maze_arg):
        """Builder works with maze_arg [[0,1,2,3], [0,1,2,3], ... ,[0,1,2,3]]."""

        self.MAZE_TRADUCTOR = {
        "0": "Path",
        "1": "Wall",
        "2": "Item",
        "3": "Guardian",
        "4": "Hero",
        }

        self.structure = []
        for y, line in enumerate(maze_arg):
            self.structure.append( \
            [Entity.factory(self.MAZE_TRADUCTOR[str(item)], x, y) \
            for x, item in enumerate(line)] \
            )

        # Same attribute definition, just ONE unreadable line:
        # self.structure = [[Entity.factory(self.MAZE_TRADUCTOR[str(item)], x, y) for x,item in enumerate(line)] for y,line in enumerate(maze_arg)]

        self.width = len(maze_arg[0])
        self.height = len(maze_arg)
        self.items_collected = 0

    # def where_the_hero(self):
    #     return filter(lambda entity: entity.__class__.__name__ == "Hero", self.structure).next()

    def console_display(self):
        # clear = lambda: os.system('cls') #on Windows System
        # clear = lambda: os.system('clear') #on Linux System
        # clear()

        trad_class_to_display = {
            "Path": " ",
            "Wall": "/",
            "Hero": "#",
            "Item": ".",
            "Guardian": "X",
        }

        debug_col_number = "   " + "".join(["   " + str(x) + "  " for x in range(self.width)])
        print(debug_col_number)

        for y,line in enumerate(self.structure):
            if len(str(y)) == 1:
                # Debug : display line numbers.
                line_to_display = "0" + str(y) + " "
            else:
                line_to_display = str(y) + " "
            for x,case in enumerate(line):
                # line_to_display += "X"
                line_to_display += trad_class_to_display[case.__class__.__name__] * 6
            print(line_to_display)
            print(line_to_display)
            print(line_to_display)
            print(line_to_display)

    # def case_scan(self, position):
    #     return self.structure[position.y][position.x].__class__.__name__

    def entity_move(self, position, goal):
        """Entities call this method when intend to move into a direction. Problem is to give the maez argument."""
        if goal.x >= 0 and goal.x < self.width and goal.y >= 0 and goal.y < self.height :
            if self.structure[goal.y][goal.x].crossable:
                print("I can go.")
                print("Goal square is: ", self.structure[goal.y][goal.x].__class__.__name__)

                if self.structure[goal.y][goal.x].__class__.__name__ == "Guardian" and self.items_collected < 3:
                    print("Sorry, you've be caught...")

                if self.structure[goal.y][goal.x].__class__.__name__ == "Guardian" and self.items_collected == 3:
                    print("CONGRATULATIONS! You escaped!")

                if self.structure[goal.y][goal.x].__class__.__name__ == "Item":
                    self.structure[goal.y][goal.x] = Entity.factory("Path", goal.x, goal.y)
                    self.items_collected += 1

                self.structure[position.y][position.x], self.structure[goal.y][goal.x] = self.structure[goal.y][goal.x], self.structure[position.y][position.x]
                return True
            else:
                print("This is a wall, I guess...")
        else:
            print("End of the maze!")
