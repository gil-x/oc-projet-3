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
    def __init__(self, position, name="item"):
        super().__init__(position)
        self.type = name

class Guardian(Entity):
    def __init__(self, position):
        super().__init__(position)

class Hero_old(Entity):

    #Class variable to get a reference to the unique instance of Hero.
    hero_list = []

    def __init__(self, position, look="down"):
        # Entity.__init__(self, position)
        super().__init__(position)
        self.look = look
        # register_instance(self)
        self.hero_list.append(self)

    # @classmethod
    # def register_instance(cls, hero):
    #     cls.hero_list.append(hero)

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


class Hero(Entity):

    def __init__(self, position, maze=None, look="down"):
        super().__init__(position)
        self.maze = maze
        self.look = look
        # self.needle = 0
        # self.barrel = 0
        # self.sedative = 0
        self.items = 0

    # def set_maze(self, maze):
    #     self.maze = maze

    def pick_item(self):
        self.items += 1

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
