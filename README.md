# PySnake

PySnake is a simple Snake game clone with some additions made with `turtle` module and OOP.

## Player Snake

By default, the snake controlled by the player starts the game at the center of the window
and its objective is to collect food and avoid fake, red-colored food, which eating resets the game.
By default, eating its own tail causes the game to restart.

## Enemy Snake

Colored red and randomly selecting its moves, this snake's objective is to
eat both food and fake food and to make the game a little bit harder.
Direct collision with its head causes the game to restart, however collision
with its tail causes the snake to shorten. This also applies to player's snake.

## Config

Some behaviours of the game and window can be changed inside `globals.py` file.
