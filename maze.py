from position import Position
from entities import Entity, Hero
import random
import os


class Maze:
    def __init__(self, maze_arg):
        """
        Builder works with maze_arg like [[0,1,2,3], [0,1,2,3], ... ,[0,1,2,3]];
        First step: randomly place 3 items to collect;
        Second step: build the maze.
        """

        self.MAZE_TRADUCTOR = {
        "0": "Path",
        "1": "Wall",
        "2": "Item",
        "3": "Guardian",
        "4": "Hero",
        }

        self.width = len(maze_arg[0])
        self.height = len(maze_arg)
        self.items_collected = 0

        # First step: place randomly 3 items in the maze.
        random_lines = random.sample(range(1, len(maze_arg)-2), 3)
        random_colums = []
        for i in random_lines:
            random_colums.append(random.choice([j for j,case in enumerate(maze_arg[i]) if case == 0]))
        for i,x in enumerate(random_lines):
            maze_arg[x][random_colums[i]] = "2"

        # Second step: Build the maze by replacing 0,1,2,3,4 by the correct object, using the Entity Factory:
        self.structure = []
        for y, line in enumerate(maze_arg):
            self.structure.append( \
            [Entity.factory(self.MAZE_TRADUCTOR[str(item)], x, y) \
            for x, item in enumerate(line)] \
            )


    def get_the_hero(self):
        """Find and returns the Hero object."""
        for y,line in enumerate(self.structure):
            for x,case in enumerate(line):
                if isinstance(case, Hero):
                    return case


    def console_display(self):
        # Dictionnary to get the correct display from Hero.look:
        trad_hero_display = {
            "down": "▼",
            "up": "▲",
            "left": "◄",
            "right": "►",
        }
        # Dictionnary to get the correct display from Hero.look:
        trad_class_to_display = {
            "Path": "░",
            "Wall": "▓",
            "Hero": trad_hero_display[str(self.get_the_hero().look)],
            "Item": ".",
            "Guardian": "X",
        }

        # Next 2 lines are only for debugging purpose - display a line of x coordonates:
        # debug_col_number = "   " + "".join(["   " + str(x) + "  " for x in range(self.width)])
        # print(debug_col_number)

        for y,line in enumerate(self.structure):
            line_to_display = ""

            # Next 4 lines are only for debugging purpose - display line number (y):
            if len(str(y)) == 1:
                line_to_display = "0" + str(y) + " "
            else:
                line_to_display = str(y) + " "

            # Iterate and display multiple times x,y to be more readable in console. '* 6' can be changed or removed:
            for x,case in enumerate(line):
                line_to_display += trad_class_to_display[type(case).__name__] * 6
            print(line_to_display)
            print(line_to_display)
            print(line_to_display)
            print(line_to_display)


    def entity_move(self, position, goal):
        """Entities call this method when intend to move into a direction. Problem is to give the maze argument."""
        if goal.x >= 0 and goal.x < self.width and goal.y >= 0 and goal.y < self.height :
            if self.structure[goal.y][goal.x].crossable:
                print("I can go.")
                print("Goal square is: ", self.structure[goal.y][goal.x].__class__.__name__)

                # If case being crossed is the guardian (exit), pragram check if hero has collected all 3 items.
                if self.structure[goal.y][goal.x].__class__.__name__ == "Guardian":
                    if self.items_collected >= 3:
                        print("CONGRATULATIONS! You escaped!")
                    else:
                        print("Sorry, you've be caught...")

                # If case to be crossed is an item, the item become a new path.
                if type(self.structure[goal.y][goal.x]).__name__ == "Item":
                    self.structure[goal.y][goal.x] = Entity.factory("Path", goal.x, goal.y)
                    self.items_collected += 1

                self.structure[position.y][position.x], self.structure[goal.y][goal.x] = self.structure[goal.y][goal.x], self.structure[position.y][position.x]
                return True
            else:
                print("This is a wall, I guess...")
        else:
            print("End of the maze!")
