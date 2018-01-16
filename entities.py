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

    # -tc- Tu peux également directement utiliser le décorateur @staticmethod
    def factory(object_type, x, y):
        if object_type == "Path":
            return Path(Position(x, y))
        elif object_type == "Wall":
            return Wall(Position(x, y))
        elif object_type == "Item":
            return Item(Position(x, y))
        elif object_type == "Guardian":
            return Guardian(Position(x, y))
        elif object_type == "Hero":
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

# -tc- Pour le héro, la notion de crossable ne fait pas de sens. Je ne pense pas que Hero
# -tc- devrait hériter de Entity
class Hero(Entity):

    #Class variable to get a reference to the unique instance of Hero.
    hero_list = []



    def __init__(self, position, look="down"):
        # Entity.__init__(self, position)
        super().__init__(position)
        self.look = look
        # register_instance(self)
        self.hero_list.append(self)
        # -tc- réfléchir comment initialiser ceci
        self.maze = maze
        self.position = position

    # @classmethod
    # def register_instance(cls, hero):
    #     cls.hero_list.append(hero)

    def move_up(self):
        if self.maze.entity_move(self.position,self.position.up):
            # -tc- si up n'est pas une propriété, il faut l'utiliser avec des parenthèses
            self.position = self.position.up()

    def move_down(self):
        if self.maze.entity_move(self.position,self.position.down):
            self.position = self.position.down

    def move_left(self):
        if self.maze.entity_move(self.position,self.position.left):
            self.position = self.position.left

    def move_right(self):
        if self.maze.entity_move(self.position,self.position.right):
            self.position = self.position.right

