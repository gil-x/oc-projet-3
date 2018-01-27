from maze import Maze
import json, os
import pygame
from pygame.locals import *

# pygame.init()

class Main:
    def __init__(self, maze_arg):
        self.maze = Maze(maze_arg)
        pygame.mixer.init()

        self.title_music = pygame.mixer.Sound("assets/sounds/8bit_title_screen.ogg")
        self.game_music = pygame.mixer.Sound("assets/sounds/espionage.ogg")
        self.item_sound = pygame.mixer.Sound("assets/sounds/rise01.ogg")
        self.win_music = pygame.mixer.Sound("assets/sounds/in_love.ogg")
        self.loss_music = pygame.mixer.Sound("assets/sounds/sad_game_over.ogg")

        self.tile_width = 35
        self.tile_height = 35

        self.window = pygame.display.set_mode((self.tile_width * self.maze.width, self.tile_height * self.maze.height), RESIZABLE)
        self.welcome = pygame.image.load("assets/welcome.png").convert()
        self.win = pygame.image.load("assets/win.png").convert()
        self.loss = pygame.image.load("assets/loss.png").convert()



        self.path = pygame.image.load("assets/path.png").convert()
        self.wall = pygame.image.load("assets/wall.png").convert()
        self.item = pygame.image.load("assets/item.png").convert_alpha()
        self.guardian = pygame.image.load("assets/guardian.png").convert_alpha()
        self.guardian.set_alpha(0.5)
        self.hero = pygame.image.load("assets/down.png").convert_alpha()
        self.hero_up = pygame.image.load("assets/top.png").convert_alpha()
        self.hero_down = pygame.image.load("assets/down.png").convert_alpha()
        self.hero_left = pygame.image.load("assets/left.png").convert_alpha()
        self.hero_right = pygame.image.load("assets/right.png").convert_alpha()
        self.hero_look = {
            "up": self.hero_up,
            "down": self.hero_down,
            "left": self.hero_left,
            "right": self.hero_right,
        }
        self.light = pygame.image.load("assets/light_cache.png").convert_alpha()




    def run(self):
        end = False

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
            self.window.blit(self.welcome, (0,0))
            self.title_music.set_volume(0.1)
            self.title_music.play()
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        self.title_music.stop()
                        end = True
                elif event.type == QUIT:
                    self.maze.quit()
                    end = True

                    # end = True #IL FAUDRAIT POUVOIR QUITTER TOTALEMENT LE JEU ICI


    def graphic_game_loop(self):
        # end = False
        self.display_2d_maze()
        self.game_music.play()
        while not self.maze.end :
        # while not self.maze.end or end: # or not end // Problème : ne finit pas le jeu ! Trouver autre chose.

            init_items = self.maze.hero.items
            hero_actual_position = self.maze.hero.position

            for event in pygame.event.get(): # PENSER à mettre elif et pas if dans ces cas.
                if event.type == QUIT:
                    self.maze.quit()
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
            self.window.blit(self.win, (0,0))
            self.win_music.play()
        else:
            self.window.blit(self.loss, (0,0))
            self.loss_music.play()
        while not end:
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == KEYDOWN or event.type == QUIT:
                    end = True


    def display_status(self):
        print("""
====================
| Items found: {items}/{nb_items} |
====================
        """.format(
        items= self.maze.hero.items,
        nb_items= self.maze.nb_items,
        ))


    def display_2d_maze(self):
        for y_position,line in enumerate(self.maze.structure):
            for x_position,case in enumerate(line):
                x = x_position * self.tile_width
                y = y_position * self.tile_height
                # CHANGER ! Et 35 devrait être dans un fichier config, dans une constante
                # D'une manière générale éviter les constantes 'magiques' = entiers glissés dans le code
                if type(case).__name__ == "Wall":
                    self.window.blit(self.wall, (x,y))
                elif type(case).__name__ == "Item":
                    self.window.blit(self.path, (x,y))
                    self.window.blit(self.item, (x,y))
                elif type(case).__name__ == "Guardian":
                    self.window.blit(self.path, (x,y))
                    self.window.blit(self.guardian, (x,y))
                elif type(case).__name__ == "Hero":
                    self.window.blit(self.path, (x,y))
                    self.hero_look["down"]
                    # if self.maze.hero.look == "down":
                    #     self.window.blit(self.hero_down, (x,y))
                    # if self.maze.hero.look == "up":
                    #     self.window.blit(self.hero_up, (x,y))
                    # if self.maze.hero.look == "left":
                    #     self.window.blit(self.hero_left, (x,y))
                    # if self.maze.hero.look == "right":
                    #     self.window.blit(self.hero_right, (x,y))
                    # self.window.blit(self.light, (x - 105,y - 105)) Ma logique n'est pas bonne... Peut être en jouant sur l'alpha des éléments (mais ça oblige à pratiquement à parcourir structure, ou créer une foction qui révise les valeurs d'alpha autour de la position : pouquoi pas...)
                else:
                    self.window.blit(self.path, (x,y))
                # self.window.blit(self.hero, (150,150))
        pygame.display.flip()

    def refresh_2d_maze(self,hero_actual_position):
        """
        Function to refreh the hero position:
        1. replace the hero by a path
        2. get hero position and draw the sprite
        """
        if self.maze.hero.distance == 1:
            self.window.blit(self.wall, (hero_actual_position.x * self.tile_width,hero_actual_position.y * self.tile_height))
        else:
            self.window.blit(self.path, (hero_actual_position.x * self.tile_width,hero_actual_position.y * self.tile_height))
        self.window.blit(self.hero_look[self.maze.hero.look], (self.maze.hero.position.x * self.tile_width,self.maze.hero.position.y * self.tile_height))
        pygame.display.flip()



with open('mazes/maze1.json', 'r') as f:
    maze_test = json.load(f)

main = Main(maze_test)
main.run()
