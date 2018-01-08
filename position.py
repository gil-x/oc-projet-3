class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def up(self):
        return Position(self.x, self.y - 1)

    @property
    def down(self):
        return Position(self.x, self.y + 1)

    @property
    def left(self):
        return Position(self.x - 1, self.y)

    @property
    def right(self):
        return Position(self.x + 1, self.y)
