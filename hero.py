# NOT USED YET!
# Future class to replace old hero, and avoid variable class to get hero position.
# Main problem is to give the Maze argument whithin a factory BEFORE this one is ready.

class Hero:

    def __init__(self, maze, position, look="down"):
        self.maze = Maze
        self.position = Position
        self.look = look
        self.needle = 0
        self.barrel = 0
        self.sedative = 0

    def move_up(self, maze):
        if maze.entity_move(self.position,self.position.up()):
            self.position = self.position.up()
    def move_down(self, maze):
        if maze.entity_move(self.position,self.position.down()):
            self.position = self.position.down()
    def move_left(self, maze):
        if maze.entity_move(self.position,self.position.left()):
            self.position = self.position.left()
    def move_right(self, maze):
        if maze.entity_move(self.position,self.position.right()):
            self.position = self.position.right()
