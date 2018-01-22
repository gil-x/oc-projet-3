from maze import Maze
import json, os
import pygame
from pygame.locals import *

# pygame.init()

class Main:
    def __init__(self, maze_arg):
        self.maze = Maze(maze_arg)

        pygame.init()

        self.window = pygame.display.set_mode((35 * self.maze.width, 35 * self.maze.height), RESIZABLE)
        self.path = pygame.image.load("assets/path.png").convert()
        self.wall = pygame.image.load("assets/wall.png").convert()
        self.hero = pygame.image.load("assets/down.png").convert()



    def run(self):
        end = False

        self.display_title_screen()


        # Main loop:
        while not self.maze.end:
            pygame.time.Clock().tick(30)
            self.display_2d_maze()
            pygame.display.flip()

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

    def display_2d_maze(self):
        for y,line in enumerate(self.maze.structure):
            for x,case in enumerate(line):
                print(case)
                if type(case).__name__ == "Path":
                    self.window.blit(self.path, (x*35,y*35))
                else:
                    self.window.blit(self.wall, (x*35,y*35))
                # self.window.blit(self.hero, (150,150))


with open('mazes/maze1.json', 'r') as f:
    maze_test = json.load(f)

main = Main(maze_test)
main.run()
