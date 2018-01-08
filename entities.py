from maze import *
from position import *

# class Square:
#     def __init__(self, position, entity=Path(position)):
#         self.position = position
#         self.entity = entity

class Entity:

    def __init__(self, position, crossable=True):
        self.position = position
        self.crossable = crossable

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

    factory = staticmethod(factory)

class Path(Entity):
    def __init__(self, position):
        super().__init__(position)
        # Entity.__init__(self, position)

class Wall(Entity):
    def __init__(self, position):
        # Entity.__init__(self, position)
        super().__init__(position)
        self.crossable = False

class Item(Entity):
    def __init__(self, position, available=True):
        # Entity.__init__(self, position)
        super().__init__(position)
        self.available = available

class Guardian(Entity):
    def __init__(self, position):
        # Entity.__init__(self, position)
        super().__init__(position)

class Hero(Entity):

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
        if maze.entity_move(self.position,self.position.up):
            self.position = self.position.up
    def move_down(self, maze):
        if maze.entity_move(self.position,self.position.down):
            self.position = self.position.down
    def move_left(self, maze):
        if maze.entity_move(self.position,self.position.left):
            self.position = self.position.left
    def move_right(self, maze):
        if maze.entity_move(self.position,self.position.right):
            self.position = self.position.right