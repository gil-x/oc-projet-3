from maze import Maze

class Main:
    def __init__(self, maze_arg):
        self.maze = Maze(maze_arg)

    def run(self):
        end = False
        hero = self.maze.get_the_hero()

        print("""
Welcome to...

=============================
|   McGyver Prozac Escape   |
=============================

(maze size: {width}x{height})
        """.format(
        width= self.maze.width,
        height= self.maze.height
        ))

        input("\nPress <ENTER> to start game!")

        # Main loop:
        while not end:
            self.maze.console_display()
            print(self.maze.get_the_hero())

            direction = input("""Where shall I go now ?
            8 = up
            2 = down
            4 = left
            6 = right
            E = quit game
            """)

            if direction == "8":
                hero.move_up(self.maze)
            elif direction == "2":
                hero.move_down(self.maze)
            elif direction == "4":
                hero.move_left(self.maze)
            elif direction == "6":
                hero.move_right(self.maze)
            elif direction == "e":
                end = True


maze_test = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,1,0,0,0,1,0,0,1,0,0,0,0,3],
[1,0,0,0,0,0,0,0,0,1,1,1,1,0,1],
[1,0,1,0,1,0,0,0,0,1,0,0,1,0,1],
[1,0,1,1,1,1,1,1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,1,0,0,0,0,1,1,1,1],
[1,0,0,1,1,0,1,1,0,0,0,1,0,0,1],
[1,0,0,0,1,0,0,1,1,1,1,1,1,0,1],
[1,0,0,1,1,1,1,1,0,0,1,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1,1,1,1,0,1],
[1,1,1,1,1,1,1,1,0,0,0,0,0,0,1],
[1,0,0,0,1,0,0,0,0,0,1,1,1,1,1],
[1,0,0,1,1,1,0,1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1,1,1,1,0,1],
[1,4,1,1,1,1,1,1,1,1,1,1,1,1,1],
]


main = Main(maze_test)
main.run()
