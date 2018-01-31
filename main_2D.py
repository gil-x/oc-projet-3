from maze import Maze
import json
import os
import glob
import random
import pygame
from pygame.locals import *
from config import *


class Main:
    def __init__(self, maze_arg):
        self.maze = Maze(maze_arg)
        pygame.mixer.init()

        self.title_music = pygame.mixer.Sound(TITLE_MUSIC)
        self.game_music = pygame.mixer.Sound(GAME_MUSIC)
        self.item_sound = pygame.mixer.Sound(ITEM_SOUND)
        self.win_music = pygame.mixer.Sound(WIN_MUSIC)
        self.loss_music = pygame.mixer.Sound(LOSS_MUSIC)

        self.window = pygame.display.set_mode((TILE_W * self.maze.width,
                TILE_H * self.maze.height), RESIZABLE)
        self.welcome = pygame.image.load(WELCOME).convert()
        self.win = pygame.image.load(WIN).convert()
        self.loss = pygame.image.load(LOSS).convert()

        self.path = pygame.image.load(PATH).convert()
        self.wall = pygame.image.load(WALL).convert()
        self.item = [
            pygame.image.load(ITEM_B).convert_alpha(),
            pygame.image.load(ITEM_S).convert_alpha(),
            pygame.image.load(ITEM_N).convert_alpha(),
            ]
        self.guardian = pygame.image.load(GUARDIAN).convert_alpha()

        self.hero = {
            "up": pygame.image.load(HERO_UP).convert_alpha(),
            "down": pygame.image.load(HERO_DOWN).convert_alpha(),
            "left": pygame.image.load(HERO_LEFT).convert_alpha(),
            "right": pygame.image.load(HERO_RIGHT).convert_alpha(),
        }
        self.first_move = True

    def display_2d_maze(self):
        for y_position, line in enumerate(self.maze.structure):
            for x_position, case in enumerate(line):
                x = x_position * TILE_W
                y = y_position * TILE_H
                if type(case).__name__ == "Wall":
                    self.window.blit(self.wall, (x, y))
                elif type(case).__name__ == "Item":
                    self.window.blit(self.path, (x, y))
                    self.window.blit(self.item.pop(), (x, y))
                elif type(case).__name__ == "Guardian":
                    self.window.blit(self.path, (x, y))
                    self.window.blit(self.guardian, (x, y))
                elif type(case).__name__ == "Hero":
                    self.window.blit(self.path, (x, y))
                    self.hero["down"]
                else:
                    self.window.blit(self.path, (x, y))

    def run(self):

        # Title screen
        self.graphic_title_loop()

        # Main loop:
        if not self.maze.quit:
            self.graphic_game_loop()

        # Ending screen
        if not self.maze.quit:
            self.graphic_end_loop()

    def graphic_title_loop(self):
        end = False
        while not end:
            self.window.blit(self.welcome, (0, 0))
            self.title_music.set_volume(0.1)
            self.title_music.play()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        self.title_music.stop()
                        end = True
                elif event.type == QUIT:
                    self.maze.exit()
                    end = True

    def refresh_2d_maze(self, hero_actual_position):
        """
        Function to refreh the hero position:
        1. replace the hero by a path
        2. get hero position and draw the sprite
        """
        if self.maze.hero.distance == 1 and self.first_move:
            self.first_move = False
            self.window.blit(self.wall,
                    (hero_actual_position.x * TILE_W,
                    hero_actual_position.y * TILE_H))
        else:
            self.window.blit(self.path,
                    (hero_actual_position.x * TILE_W,
                    hero_actual_position.y * TILE_H))

        self.window.blit(self.hero[self.maze.hero.look],
                (self.maze.hero.position.x * TILE_W,
                self.maze.hero.position.y * TILE_H))
        pygame.display.flip()

    def graphic_game_loop(self):
        end = False
        self.display_2d_maze()
        self.game_music.play()
        heros_initial_position = self.maze.hero.position

        while not self.maze.end and not end:
            init_items = self.maze.hero.items
            hero_actual_position = self.maze.hero.position

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.maze.exit()
                    end = True
                if event.type == KEYDOWN:
                    if event.key == K_UP:
                        self.maze.hero.move_up(self.maze)
                    elif event.key == K_DOWN:
                        self.maze.hero.move_down(self.maze)
                    elif event.key == K_LEFT:
                        self.maze.hero.move_left(self.maze)
                    elif event.key == K_RIGHT:
                        self.maze.hero.move_right(self.maze)
                self.refresh_2d_maze(hero_actual_position)
                if init_items != self.maze.hero.items:
                    self.item_sound.play()

    def graphic_end_loop(self):
        self.game_music.stop()
        end = False
        if self.maze.hero.items >= self.maze.nb_items:
            self.window.blit(self.win, (0, 0))
            self.win_music.play()
        else:
            self.window.blit(self.loss, (0, 0))
            self.loss_music.play()
        while not end:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == KEYDOWN or event.type == QUIT:
                    end = True


def load_mazes():
    maze_files = []
    choice = -1
    for maze_file in glob.glob("./mazes/*.json"):
        maze_files.append(maze_file)

    if len(maze_files) > 1:
        f = random.choice(maze_files).replace("\\", "/").replace("./", "")
    else:
        f = 'mazes/default.json'

    with open(f, 'r') as f:
        maze_arg = json.load(f)
    return maze_arg


main = Main(load_mazes())
main.run()
