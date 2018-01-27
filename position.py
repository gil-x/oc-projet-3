class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def up(self):
        return Position(self.x, self.y - 1)

    def down(self):
        return Position(self.x, self.y + 1)

    def left(self):
        return Position(self.x - 1, self.y)

    def right(self):
        return Position(self.x + 1, self.y)

    def look_around(self):
        return [Position(self.x, self.y - 1), Position(self.x, self.y + 1), Position(self.x - 1, self.y), Position(self.x + 1, self.y)]
