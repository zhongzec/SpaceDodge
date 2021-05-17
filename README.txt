--------------------------------------------------------------------------------
0. Please use python 2
--------------------------------------------------------------------------------
1. Files

run.py: parse arguments and start game
game.py: game logic and interaction
window.py: game window logic
player.py: player logc and interaction
obstacle.py: obstacle logic

--------------------------------------------------------------------------------
2. How to start

python ./run.py --canvas_height 20 --canvas_width 50 --diff_level 1

or

python ./run.py -h 20 -w 80 -d 1

Note: height and width of canvas are determined by the maximum allowed by current
Terminal size
--------------------------------------------------------------------------------
3. How to play

A or KeyLeft: move player left
D or KeyRight: move player right
W or KeyUp: move player up
S or KeyDown: move player down
ESC: exit game

Game will be exited 3 seconds after player hit the obstacles
--------------------------------------------------------------------------------

Note: The scoring system works as counting the number of passed dropping obstacles
which reached the last level of the canvas
