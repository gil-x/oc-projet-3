import json, os
import pygame
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
        self.window = pygame.display.set_mode((self.tile_width * len(self.structure[0]), self.tile_height * len(self.structure)), RESIZABLE)

        self.path = pygame.image.load("assets/path.png").convert()
        self.wall = pygame.image.load("assets/wall.png").convert()
        self.guardian = pygame.image.load("assets/guardian.png").convert_alpha()
        self.hero = pygame.image.load("assets/down.png").convert_alpha()



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


    def run(self):
        self.display_2d_maze()

        end = False
        while not end:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == QUIT:
                    end = True
                if event.type == pygame.MOUSEBUTTONUP:
                # if pygame.mouse.get_pressed()[0]:
                    mouse = pygame.mouse.get_pos()
                    print(pygame.mouse.get_pos())
                    print(type(pygame.mouse.get_pos()))
                    x = mouse[0] // self.tile_width
                    y = mouse[1] // self.tile_height
                    print('x=',x)
                    print('y=',y)
                    if x != 0 and x != len(self.structure[0]) - 1 and y != 0 and y != len(self.structure) - 1:
                        if self.structure[y][x] == 0:
                            self.window.blit(self.wall, (x * self.tile_width, y * self.tile_height))
                            self.structure[y][x] = 1
                        elif self.structure[y][x] == 1:
                            self.window.blit(self.path, (x * self.tile_width, y * self.tile_height))
                            self.structure[y][x] = 0


main = Main(base)
main.run()
