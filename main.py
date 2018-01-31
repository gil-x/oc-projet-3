from maze import Maze
import json, os, glob

class Main:
    def __init__(self, maze_arg):
        self.maze = Maze(maze_arg)

    def run(self):
        end = False
        self.display_title_screen()

        # Main loop:
        while not self.maze.end:
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
        # Uncomment the lines accordind to your system:
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
| Distance: {distance}
====================
        """.format(
        items= self.maze.hero.items,
        nb_items= self.maze.nb_items,
        distance= self.maze.hero.distance,
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


def load_mazes():
    maze_files = []
    choice = -1
    for maze_file in glob.glob("./mazes/*.json"):
        maze_files.append(maze_file)
    maze_files_presentation = ""
    for i,maze_file in enumerate(maze_files):
        maze_files_presentation += "{i} = {name}\n".format(
            i=str(i),
            name=maze_file.replace("./mazes\\", ""),
        )
    print(maze_files_presentation)
    while choice not in range(0, len(maze_files)):
        choice = int(input("Wich one?\n"))
    f = glob.glob("./mazes/*.json")[choice].replace("\\", "/").replace("./", "")
    with open(f, 'r') as f:
        maze_arg = json.load(f)
    return maze_arg

maze_arg = load_mazes()

main = Main(maze_arg)
main.run()
