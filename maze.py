from position import Position
from entities import Entity, Hero
import random

MAZE_TRADUCTOR = {
"0": "Path",
"1": "Wall",
"2": "Item",
"3": "Guardian",
"4": "Hero",
}


class Maze:
    def __init__(self, maze_arg, nb_items=3):
        """
        Builder works with maze_arg like [[0,1,2,3], [0,1,2,3], ... ,[0,1,2,3]];
        First step: randomly place 3 items to collect;
        Second step: build the maze.
        """
        self.end = False
        self.quit = False
        self.config = maze_arg
        self.width = len(maze_arg[0])
        self.height = len(maze_arg)
        self.console_w = 4
        self.console_h = 2
        self.nb_items = nb_items

        self.place_items2(maze_arg)

        self.hero = self.get_the_hero()

    def exit(self):
        self.quit = True

    def place_items(self, maze_arg):
        random_lines = random.sample(range(1, len(maze_arg)-1), self.nb_items)
        random_colums = []
        for i in random_lines:
            random_colums.append(random.choice([j for j,case in enumerate(maze_arg[i]) if case == 0]))
        for i,x in enumerate(random_lines):
            maze_arg[x][random_colums[i]] = "2"

        # Second step: Build the maze by replacing 0,1,2,3,4 by the correct object, using the Entity Factory:
        self.structure = []
        for y, line in enumerate(maze_arg):
            self.structure.append( \
            [Entity.factory(MAZE_TRADUCTOR[str(item)], x, y) \
            for x, item in enumerate(line)] \
            )

    def place_items2(self, maze_arg):
        positions_availables = []
        for y,line in enumerate(maze_arg):
            for x,tile in enumerate(line):
                if tile == 0:
                    positions_availables.append((x,y))
        print('positions_availables:',positions_availables)
        tiles = random.sample(positions_availables,self.nb_items)
        print('tiles:',tiles,x,y)
        for tile in tiles:
            maze_arg[tile[0]][tile[1]] = "2"

        # Second step: Build the maze by replacing 0,1,2,3,4 by the correct object, using the Entity Factory:
        self.structure = []
        for y, line in enumerate(maze_arg):
            self.structure.append( \
            [Entity.factory(MAZE_TRADUCTOR[str(item)], x, y) \
            for x, item in enumerate(line)] \
            )

    def get_the_hero(self):
        """Find and returns the Hero object."""
        for y,line in enumerate(self.structure):
            for x,entity in enumerate(line):
                if isinstance(entity, Hero):
                    return entity

    def get_square(self,position):
        return self.structure[position.y][position.x]

    def set_square(self,position,entity):
        self.structure[position.y][position.x] = entity

    def console_display(self):
        # Dictionnary to get the correct display from Hero.look:
        trad_hero_display = {
            "down": "▼",
            "up": "▲",
            "left": "◄",
            "right": "►",
        }
        # trad_item_display = {
        #     "needle": "n",
        #     "barrel": "b",
        #     "sedative": "s",
        # }
        # Dictionnary to get the correct display from Hero.look:
        trad_class_to_display = {
            "Path": "░",
            "Wall": "▓",
            "Hero": trad_hero_display[str(self.hero.look)],
            "Item": ".",
            "Guardian": "X",
        }

        # Next 2 lines are only for debugging purpose - display a line of x coordonates:
        # debug_col_number = "   " + "".join(["   " + str(x) + "  " for x in range(self.width)])
        # print(debug_col_number)

        for y,line in enumerate(self.structure):
            line_to_display = ""

            # Next 4 lines are only for debugging purpose - display line number (y):
            # if len(str(y)) == 1:
            #     line_to_display = "0" + str(y) + " "
            # else:
            #     line_to_display = str(y) + " "

            # Iterate and display multiple times x,y to be more readable in console. '* 6' can be changed or removed:
            for x,case in enumerate(line):
                line_to_display += trad_class_to_display[type(case).__name__] * self.console_w
            for i in range(self.console_h):
                print(line_to_display)



    def entity_move(self, position, goal):
        """
        Entities call this method when intend to move into a direction. Problem is to give the maze argument.
        Args: position, goal = Postion instances.
        """
        if goal.x >= 0 and goal.x < self.width and goal.y >= 0 and goal.y < self.height :
            if self.get_square(goal).crossable:
                # print("I can go.")
                # print("Goal get_square is: ", type(self.get_square(goal)).__name__)
                self.hero.add_distance()

                # If case being crossed is the guardian (exit), pragram check if hero has collected all 3 items.

                # if type(self.get_square(goal.look_around())).__name__ == "Guardian": # ON PEUT FAIRE MIEUX AVEC isinstance et Guardian sans ""
                if "Guardian" in [type(self.get_square(position)).__name__ for position in goal.look_around()]: # ON PEUT FAIRE MIEUX AVEC isinstance et Guardian sans "" MAIS il faut importer les autres classes.
                    self.end = True

                # If case to be crossed is an item, the item become a new path.
                elif type(self.structure[goal.y][goal.x]).__name__ == "Item":
                    self.structure[goal.y][goal.x] = Entity.factory("Path", goal.x, goal.y)
                    self.hero.pick_item()

                self.set_square(goal, self.get_square(position))
                if self.hero.distance == 1:
                    self.set_square(position, Entity.factory("Wall", goal.x, goal.y))
                else:
                    self.set_square(position, Entity.factory("Path", goal.x, goal.y))
                return True
            else:
                print("This is a wall, I guess...")
                pass
        else:
            print("End of the maze!")
