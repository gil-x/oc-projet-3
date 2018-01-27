from position import Position


class Entity:
    """Main class, from which other entities heritate. Not used herself."""

    def __init__(self, position, crossable=True):
        self.position = position
        self.crossable = crossable

    @staticmethod
    def factory(object_type, x, y):
        if object_type == "Path":
            return Path(Position(x, y))
        if object_type == "Wall":
            return Wall(Position(x, y))
        if object_type == "Item":
            return Item(Position(x, y))
        if object_type == "Guardian":
            return Guardian(Position(x, y))
        if object_type == "Hero":
            return Hero(Position(x, y))


class Path(Entity):
    def __init__(self, position):
        super().__init__(position)

class Wall(Entity):
    def __init__(self, position):
        super().__init__(position)
        self.crossable = False

class Item(Entity):
    NAMES = ["needle", "barrel", "sedative"]
    def __init__(self, position, name="item"):
        super().__init__(position)
        self.type = self.NAMES.pop()

class Guardian(Entity):
    def __init__(self, position, vigilant=True):
        super().__init__(position)
        self.vigilant = vigilant


class Hero(Entity):

    def __init__(self, position, maze=None, look="down"):
        super().__init__(position)
        self.maze = maze
        self.look = look
        self.needle = 0
        self.barrel = 0
        self.sedative = 0
        self.items = 0
        self.distance = 0


    def pick_item(self):
        self.items += 1

    def add_distance(self):
        self.distance += 1

    def move_up(self, maze):
        self.look = "up"
        if maze.entity_move(self.position,self.position.up()):
            self.position = self.position.up()
    def move_down(self, maze):
        self.look = "down"
        if maze.entity_move(self.position,self.position.down()):
            self.position = self.position.down()
    def move_left(self, maze):
        self.look = "left"
        if maze.entity_move(self.position,self.position.left()):
            self.position = self.position.left()
    def move_right(self, maze):
        self.look = "right"
        if maze.entity_move(self.position,self.position.right()):
            self.position = self.position.right()
