Little maze game created with Python for a student course for
"Openclassrooms | parcours développeur d'applications Python",
project 3 "Projet 3 : "Aidez MacGyver à s'échapper !"":


MCGYVER PROZAC CRAZY ESCAPE


*** Story:
McGyver was caught trying to make a nuclear bomb with some corn flakes and wire.
Locked up in a psychiatric hospital, he has an escape plan: find enough medical
stuff to make the guardian asleep and get out of.


*** Play the game:
Look at requirement.txt and install the modules indicated.
You can run the game either in console or graphic window:
- console: run main.py
- graphic: run main_2D.py


*** Win the game:
Three items are randomly put in the maze, you have to collect all before reach
the guardian and end the game.


*** Create levels:
You can create levels by using editor.py: just run it!
Follow instructions written in the bottom on the screen.
But BE AWARE of two thin:
- dont make tiles not crossables or put the hero or guardian in backends;
- very important: keep in mind that when the hero step aside the guardian, game
ends, so do NOT create tiles crossables after bypass the guardian: it should be
impossible to get some items and win the game;
- you press ENTER to register the created maze in "mazes" folder as "custom.json",
you can rename it and create anothers mazes as you want;
- in console game you choose the maze from all in "mazes" folder;
- in graphic game, the maze is randomly picked in the "mazes" folder;


*** Custom graphics and sounds:
You can do that : look in config.py and best practice create and change the
ASSETS_PATH to "my_assets" or what you want. Next you should use the same names
for each musics, sounds and graphics. Beware to use same formats: ogg & png.
