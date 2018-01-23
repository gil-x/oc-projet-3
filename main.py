from maze import Maze
import json, os

class Main:
    def __init__(self, maze_arg):
        self.maze = Maze(maze_arg)

    def run(self):
        end = False

        self.display_title_screen()

        # Main loop:
        while not self.maze.end: # tester si un des deux end est True / pour faire un quit & save par exemple.

            self.maze.console_display()
            self.display_status()

            direction = input("""Where shall I go now ?
            8 = up
            2 = down
            4 = left
            6 = right
            Q = quit game
            """)

            if direction == "8":
                self.maze.hero.move_up(self.maze)
            elif direction == "2":
                self.maze.hero.move_down(self.maze)
            elif direction == "4":
                self.maze.hero.move_left(self.maze)
            elif direction == "6":
                self.maze.hero.move_right(self.maze)
            elif direction == "q":
                break

            self.clear_console()

        # Display result:
        if self.maze.hero.items >= self.maze.nb_items:
            self.display_victory_screen()
        else:
            self.display_loss_screen()


    def clear_console(self):
        clear = lambda: os.system('cls') # Windows System
        # clear = lambda: os.system('clear') # Linux System
        clear()


    def display_title_screen(self):
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
        self.clear_console()


    def display_status(self):
        print("""
====================
| Items found: {items}/{nb_items} |
====================
        """.format(
        items= self.maze.hero.items,
        nb_items= self.maze.nb_items,
        ))


    def display_victory_screen(self):
        print("""
*************************************
*                                   *
*   CONGRATULATIONS! You escaped!   *
*                                   *
*************************************
""")
        input("\n\n\nPress <ENTER> to quit.")


    def display_loss_screen(self):
        print("""
--------------------------
Sorry, you've be caught...
--------------------------
""")
        input("\n\n\nPress <ENTER> to quit.")


with open('mazes/maze1.json', 'r') as f:
    maze_test = json.load(f)

# maze_test = [
# [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
# [1,0,1,0,0,0,1,0,0,1,0,0,0,0,3],
# [1,0,0,0,0,0,0,0,0,1,1,1,1,0,1],
# [1,0,1,0,1,0,0,0,0,1,0,0,1,0,1],
# [1,0,1,1,1,1,1,1,0,0,0,0,0,0,1],
# [1,0,0,0,0,0,1,0,0,0,0,1,1,1,1],
# [1,0,0,1,1,0,1,1,0,0,0,1,0,0,1],
# [1,0,0,0,1,0,0,1,1,1,1,1,1,0,1],
# [1,0,0,1,1,1,1,1,0,0,1,0,0,0,1],
# [1,0,0,0,0,0,0,0,0,1,1,1,1,0,1],
# [1,1,1,1,1,1,1,1,0,0,0,0,0,0,1],
# [1,0,0,0,1,0,0,0,0,0,1,1,1,1,1],
# [1,0,0,1,1,1,0,1,0,0,0,0,0,0,1],
# [1,0,0,0,0,0,0,0,0,1,1,1,1,0,1],
# [1,4,1,1,1,1,1,1,1,1,1,1,1,1,1],
# ]

# with open('mazes/maze1.json', 'w') as f:
#     f.write(json.dumps(maze_test, indent=4))

main = Main(maze_test)
main.run()
