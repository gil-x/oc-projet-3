Openclassrooms | parcours développeur d'applications Python

--
Projet 3 : "Aidez MacGyver à s'échapper !"
--

Contexte du jeu :

McGyver Prozac Crazy Escape. McGyver a été interné, il peut s'enfuir s'il trouve de quoi endormir le garde qui surveille la sortie de l'hôpital.


VERSIONS
--

0.1 - It's working but code is not pythonic.

0.4 - Console version works but need some improvements

Done in this version:
- class Main added in main.py ;
- random set up for items ;
- position.[direction] properties are now methods ;
- Maze displays following direction asked ; more doc.

Need to:
- use a new class Hero, not child of Entity, which manage the collected items and which instance should be initialized with the correct Maze instance (big problem to solve!).


0.41 - Console version works but need some improvements / imports fixed / added unused new standalone Hero class

Done in this version:
- imports fixed and pythonics (I hope...)

Need to:
- use a new class Hero, not child of Entity, which manage the collected items and which instance should be initialized with the correct Maze instance (big problem to solve!).


0.5 - Console version works but need some improvements / imports fixed / added unused new standalone Hero class

Done in this version:
- Maze tell when the game ends to main ;
- mains sections of the game are now in displayed by separate functions in Main (easier to create other main display modules) ;
- better console presentation ;
- now maze is loaded from a json file ;
- begun main_2D.py, will work with pygame.

Need to:
- use a new class Hero, not child of Entity, which manage the collected items and which instance should be initialized with the correct Maze instance (big problem to solve!) ;
- write a module to create mazes as json, or convert txt/csv to json ;
- explore and choose which maze to play ;
- a big loop to replay/change maze ;
