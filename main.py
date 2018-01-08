from maze import *
from entities import *
from position import *

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

maze1 = Maze(maze_test)
hero = Hero.hero_list[0]

print("Maze.width: ",maze1.width)
print("Maze.height: ",maze1.height)
print("Hero x = ", hero.position.x, " | ","Hero y = ", hero.position.y)

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

while 1:
    print("items collected: ",maze1.items_collected,"/3.")

    direction = input("""Where shall I go now ?
    8 = up
    2 = down
    4 = left
    6 = right
    E = quit game
    """)

    if direction == "8":
        hero.move_up(maze1)
    elif direction == "2":
        hero.move_down(maze1)
    elif direction == "4":
        hero.move_left(maze1)
    elif direction == "6":
        hero.move_right(maze1)
    elif direction == "e":
        break
    maze1.console_display()

# maze1.entity_move(hero.position,hero.position.up)






input("\nPRESS ENTER")
