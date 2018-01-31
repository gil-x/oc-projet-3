import pygame as pg
import json
import os
from config import *
from pygame.locals import *

pg.init()


class Main:
    def __init__(self, maze_arg):
        self.structure = maze_arg

        self.window = pg.display.set_mode((TILE_W * len(self.structure[0]),
                TILE_H * len(self.structure) + 50), RESIZABLE)

        self.path = pg.image.load("assets/path.png").convert()
        self.wall = pg.image.load("assets/wall.png").convert()
        self.guardian = pg.image.load("assets/guardian.png").convert_alpha()
        self.hero = pg.image.load("assets/down.png").convert_alpha()

        self.max_x = len(self.structure[0]) - 1
        self.max_y = len(self.structure) - 1

    def display_2d_maze(self):
        end = False
        pg.display.flip()
        for y_position, line in enumerate(self.structure):
            for x_position, tile in enumerate(line):
                x = x_position * TILE_W
                y = y_position * TILE_H
                if tile == 0:
                    self.window.blit(self.path, (x, y))
                elif tile == 1:
                    self.window.blit(self.wall, (x, y))
                elif tile == 3:
                    self.window.blit(self.path, (x, y))
                    self.window.blit(self.guardian, (x, y))
                elif tile == 4:
                    self.window.blit(self.path, (x, y))
                    self.window.blit(self.hero, (x, y))

    def refresh_message(self,text):
        rect = pg.draw.rect(self.window, (0, 0, 0), pg.Rect(0, 525, 525, 50))
        font = pg.font.SysFont(pg.font.get_default_font(),
                20, bold=False, italic=False)
        message = font.render(text, True, (200, 255, 100))
        self.window.blit(message, (35, TILE_H * len(self.structure) + 20))
        pg.display.update()

    def run(self):
        self.display_2d_maze()
        self.refresh_message("""
        Click to add/remove walls. Press ENTER to save maze as 'custom'.
        """)

        end = False
        placing_guardian = False
        placing_hero = False

        while not end:
            pg.display.flip()

            for event in pg.event.get():
                if event.type == QUIT:
                    end = True
                elif event.type == pg.MOUSEBUTTONUP:
                    mouse = pg.mouse.get_pos()
                    x = mouse[0] // TILE_W
                    y = mouse[1] // TILE_H

                    if y > self.max_y:
                        pass

                    elif self.structure[y][x] == 3 and not placing_hero:
                        self.window.blit(self.wall, (x * TILE_W, y * TILE_H))
                        self.structure[y][x] = 1
                        placing_guardian = True
                        self.refresh_message("""Your're holding the Exit/Guardian, drop him on an external wall.""")

                    elif self.structure[y][x] == 4 and not placing_guardian:
                        self.window.blit(self.wall, (x * TILE_W, y * TILE_H))
                        self.structure[y][x] = 1
                        placing_hero = True
                        self.refresh_message("Your're holding the Hero, drop him on an external wall.")

                    elif (x == 0 or x == self.max_x or y == 0 or y == self.max_y) \
                            and ((x,y) not in [(0,0),(0,14),(14,0),(14,14)]) \
                            and placing_guardian and self.structure[y][x] != 4:
                        self.window.blit(self.path, (x * TILE_W, y * TILE_H))
                        self.window.blit(self.guardian, (x * TILE_W, y * TILE_H))
                        self.structure[y][x] = 3
                        placing_guardian = False
                        self.refresh_message("Click to add/remove walls. Press ENTER to save maze as 'custom'.")

                    elif (x == 0 or x == self.max_x or y == 0 or y == self.max_y) \
                            and ((x,y) not in [(0,0),(0,14),(14,0),(14,14)]) \
                            and placing_hero and self.structure[y][x] != 3:
                        self.window.blit(self.path, (x * TILE_W, y * TILE_H))
                        self.window.blit(self.hero, (x * TILE_W, y * TILE_H))
                        self.structure[y][x] = 4
                        placing_hero = False
                        self.refresh_message("Click to add/remove walls. Press ENTER to save maze as 'custom'.")

                    elif x != 0 and x != self.max_x and y != 0 and y != self.max_y:
                        if self.structure[y][x] == 0:
                            self.window.blit(self.wall,
                                    (x * TILE_W, y * TILE_H))
                            self.structure[y][x] = 1
                        elif self.structure[y][x] == 1:
                            self.window.blit(self.path,
                                    (x * TILE_W, y * TILE_H))
                            self.structure[y][x] = 0


                elif event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        with open('mazes/custom.json', 'w') as maze_file:
                            json.dump(self.structure, maze_file)
                            pass
                        end = True

main = Main(BASE)
main.run()
