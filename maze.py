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
        Builder works with maze_arg like [[0,1,2,3], ... ,[0,1,2,3]];
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
        self.place_items(maze_arg)
        self.hero = self.get_the_hero()

    def exit(self):
        self.quit = True

    def place_items(self, maze_arg):
        positions_availables = []
        for y, line in enumerate(maze_arg):
            for x, tile in enumerate(line):
                if tile == 0:
                    positions_availables.append((x, y))
        tiles = random.sample(positions_availables, self.nb_items)

        for tile in tiles:
            maze_arg[tile[0]][tile[1]] = "2"

        # Second step: Build the maze by replacing 0,1,2,3,4
        # by the correct object, using the Entity Factory:
        self.structure = []
        for y, line in enumerate(maze_arg):
            self.structure.append(
            [Entity.factory(MAZE_TRADUCTOR[str(item)], x, y)
            for x, item in enumerate(line)]
            )

    def get_the_hero(self):
        """Find and returns the Hero object."""
        for y, line in enumerate(self.structure):
            for x, entity in enumerate(line):
                if isinstance(entity, Hero):
                    return entity

    def get_square(self, position):
        return self.structure[position.y][position.x]

    def set_square(self, position, entity):
        self.structure[position.y][position.x] = entity

    def console_display(self):
        # Dictionnary to get the correct display from Hero.look:
        trad_hero_display = {
            "down": "▼",
            "up": "▲",
            "left": "◄",
            "right": "►",
        }
        trad_class_to_display = {
            "Path": "░",
            "Wall": "▓",
            "Hero": trad_hero_display[str(self.hero.look)],
            "Item": ".",
            "Guardian": "X",
        }

        for y, line in enumerate(self.structure):
            line_to_display = ""
            for x, case in enumerate(line):
                line_to_display += \
                trad_class_to_display[type(case).__name__] * self.console_w
            for i in range(self.console_h):
                print(line_to_display)

    def entity_move(self, position, goal):
        """
        Entities call this method when intend to move into a direction.
        Args: position, goal = Position instances.
        """
        if goal.x >= 0 and goal.x < self.width and goal.y >= 0 and \
                goal.y < self.height:
            if self.get_square(goal).crossable:
                self.hero.add_distance()

                # If case to be crossed is an item, the item become a new path.
                if type(self.structure[goal.y][goal.x]).__name__ == "Item":
                    # self.hero.pick_item()
                    self.hero.pick_named_item(self.structure[goal.y][goal.x].name)
                    self.hero.display_items()
                    self.structure[goal.y][goal.x] = Entity.factory("Path",
                            goal.x, goal.y)

                if "Guardian" in [type(self.get_square(position)).__name__
                        for position in goal.look_around()]:
                    self.end = True

                self.set_square(goal, self.get_square(position))
                if self.hero.distance == 1:
                    self.set_square(position, Entity.factory("Wall",
                            goal.x, goal.y))
                else:
                    self.set_square(position, Entity.factory("Path",
                            goal.x, goal.y))
                return True
            else:
                print("This is a wall, I guess...")
                pass
        else:
            print("End of the maze!")
