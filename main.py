# -tc- Eviter la syntaxe: from module import *
from maze import *

# -tc- A quoi correspondent 2, 3 et 4 ?
maze_test = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,1,0,0,2,1,0,0,1,0,0,0,0,3],
[1,0,0,0,0,0,0,0,0,1,1,1,1,0,1],
[1,0,1,0,1,0,0,0,0,1,0,0,1,0,1],
[1,0,1,1,1,1,1,1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,1,0,0,0,0,1,1,1,1],
[1,0,0,1,1,0,1,1,0,0,0,1,0,0,1],
[1,0,0,0,1,0,0,1,1,1,1,1,1,0,1],
[1,0,0,1,1,1,1,1,0,0,1,0,0,0,1],
[1,0,0,0,0,2,0,0,0,1,1,1,1,0,1],
[1,1,1,1,1,1,1,1,0,0,0,0,0,0,1],
[1,0,0,0,1,0,0,0,0,0,1,1,1,1,1],
[1,2,0,1,1,1,0,1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1,1,1,1,0,1],
[1,4,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

# -tc- Il sera possible de mettre le code de fichier dans une classe avec
# -tc- deux méthodes: 1/ __init__ pour l'initialisation et 2/ run ou start pour
# -tc- la boucle de jeu
maze1 = Maze(maze_test)
hero = Hero(maze)
#hero = Hero.hero_list[0]

print("Maze.width: ",maze1.width)
print("Maze.height: ",maze1.height)
print("Hero x = ", hero.position.x, " | ","Hero y = ", hero.position.y)

# -tc- J'afficherais personnellement le labyrinthe uniquement dans la boucle de jeu
maze1.console_display()
# position1 = Position(5,1)
# print(maze1.case_scan(position1))
# print(Hero.hero_list[0])


# direction_traductor = {
# "8": hero.move_up(maze1),
# "2": hero.move_down(maze1),
# "4": hero.move_left(maze1),
# "6": hero.move_right(maze1),
# }

end = False
while not end:
    print("items collected: ",maze1.items_collected,"/3.")
    # -tc- J'afficherais personnellement le labyrinthe en début de boule
    maze1.console_display()

    direction = input("""Where shall I go now ?
    8 = up
    2 = down
    4 = left
    6 = right
    E = quit game
    """)

    if direction == "8":
        # -tc- plutôt que de passer maze1 à chaque fois à move_*, autant le passer
        # -tc- une seule fois à la construction de hero (via Hero.__init__)
        hero.move_up()
    elif direction == "2":
        hero.move_down()
    elif direction == "4":
        hero.move_left()
    elif direction == "6":
        hero.move_right()
    elif direction == "e":
        end = True

# maze1.entity_move(hero.position,hero.position.up)






input("\nPRESS ENTER")
