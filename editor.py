import json, os
import pygame, json
from pygame.locals import *

pygame.init()

base = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,3],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,4,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

class Main:
    def __init__(self, maze_arg):
        self.structure = maze_arg

        self.tile_width = 35
        self.tile_height = 35
        self.window = pygame.display.set_mode((self.tile_width * len(self.structure[0]), self.tile_height * len(self.structure) + 50), RESIZABLE)

        self.path = pygame.image.load("assets/path.png").convert()
        self.wall = pygame.image.load("assets/wall.png").convert()
        self.guardian = pygame.image.load("assets/guardian.png").convert_alpha()
        self.hero = pygame.image.load("assets/down.png").convert_alpha()

        self.max_x = len(self.structure[0]) - 1
        self.max_y = len(self.structure) - 1

    def display_2d_maze(self):
        end = False
        pygame.display.flip()
        for y_position,line in enumerate(self.structure):
            for x_position,tile in enumerate(line):
                x = x_position * self.tile_width
                y = y_position * self.tile_height
                if tile == 0:
                    self.window.blit(self.path, (x,y))
                elif tile == 1:
                    self.window.blit(self.wall, (x,y))
                elif tile == 3:
                    self.window.blit(self.path, (x,y))
                    self.window.blit(self.guardian, (x,y))
                elif tile == 4:
                    self.window.blit(self.path, (x,y))
                    self.window.blit(self.hero, (x,y))

    def refresh_message(self,text):
        rect = pygame.draw.rect(self.window, (0,0,0), pygame.Rect(0, 525, 525, 50))
        font = pygame.font.SysFont(pygame.font.get_default_font(), 20, bold=False, italic=False)
        message = font.render(text,True,(200,255,100))
        self.window.blit(message,(35, self.tile_height * len(self.structure) + 20))
        pygame.display.update()

    def run(self):
        self.display_2d_maze()
        self.refresh_message("Click to add/remove walls. Press ENTER to save maze as 'custom'.")

        end = False
        placing_guardian = False
        placing_hero = False

        while not end:
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == QUIT:
                    end = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse = pygame.mouse.get_pos()
                    x = mouse[0] // self.tile_width
                    y = mouse[1] // self.tile_height

                    if self.structure[y][x] == 3 and not placing_hero:
                        self.window.blit(self.wall, (x * self.tile_width, y * self.tile_height))
                        self.structure[y][x] = 1
                        placing_guardian = True
                        self.refresh_message("Your're holding the Exit/Guardian, drop him on an external wall.")

                    elif self.structure[y][x] == 4 and not placing_guardian:
                        self.window.blit(self.wall, (x * self.tile_width, y * self.tile_height))
                        self.structure[y][x] = 1
                        placing_hero = True
                        self.refresh_message("Your're holding the Hero, drop him on an external wall.")


                    elif (x == 0 or x == self.max_x or y == 0 or y == self.max_y) and placing_guardian and self.structure[y][x] != 4:
                        self.window.blit(self.path, (x * self.tile_width, y * self.tile_height))
                        self.window.blit(self.guardian, (x * self.tile_width, y * self.tile_height))
                        self.structure[y][x] = 3
                        placing_guardian = False
                        self.refresh_message("Click to add/remove walls. Press ENTER to save maze as 'custom'.")

                    elif (x == 0 or x == self.max_x or y == 0 or y == self.max_y) and placing_hero and self.structure[y][x] != 3:
                        self.window.blit(self.path, (x * self.tile_width, y * self.tile_height))
                        self.window.blit(self.hero, (x * self.tile_width, y * self.tile_height))
                        self.structure[y][x] = 4
                        placing_hero = False
                        self.refresh_message("Click to add/remove walls. Press ENTER to save maze as 'custom'.")

                    elif x != 0 and x != self.max_x and y != 0 and y != self.max_y:
                        print(placing_guardian, "3")
                        if self.structure[y][x] == 0:
                            self.window.blit(self.wall, (x * self.tile_width, y * self.tile_height))
                            self.structure[y][x] = 1
                        elif self.structure[y][x] == 1:
                            self.window.blit(self.path, (x * self.tile_width, y * self.tile_height))
                            self.structure[y][x] = 0

                elif event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        with open('mazes/custom.json', 'w') as maze_file:
                            json.dump(self.structure, maze_file)
                            pass
                        end = True

main = Main(base)
main.run()
