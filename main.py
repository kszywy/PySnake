from turtle import Screen
from globals import WINDOW_HEIGHT, WINDOW_WIDTH, BORDER_MODE, TAIL_MODE, SNAKE_LENGTH
from snake import Snake
from enemysnake import EnemySnake
from food import Food, FakeFood
from scoreboard import Scoreboard
import time

# Window setup
window = Screen()
window.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
window.bgcolor("black")
window.title("My Snake Game")
window.tracer(0)

# Object definitions
player_snake = Snake(SNAKE_LENGTH)
enemy_snake = EnemySnake(SNAKE_LENGTH * 4)
scoreboard = Scoreboard()
food = Food()
fakefood = FakeFood()

# Event listeners
window.listen()
window.onkey(player_snake.up, "Up")
window.onkey(player_snake.left, "Left")
window.onkey(player_snake.right, "Right")
window.onkey(player_snake.down, "Down")

# Main loop
while not player_snake.is_dead():
    window.update()
    time.sleep(0.1)
    player_snake.move_forward()
    enemy_snake.random_move()
    enemy_snake.move_forward()

    # Detect collision with an enemy
    enemy_bite = Snake.which_enemy_segment_is_bitten(player_snake, enemy_snake)
    if enemy_bite == 0:
        player_snake.die(SNAKE_LENGTH)
        enemy_snake.die(SNAKE_LENGTH * 4)
        scoreboard.reset_score()
    elif enemy_bite != -1:
        Snake.enemy_collision(enemy_bite, enemy_snake)

    # Detect collision with player
    player_bite = Snake.which_enemy_segment_is_bitten(enemy_snake, player_snake)
    if player_bite == 0:
        player_snake.die(SNAKE_LENGTH * 4)
        enemy_snake.die(SNAKE_LENGTH)
    elif player_bite != -1:
        Snake.enemy_collision(player_bite, player_snake)

    # Detect player collision with food
    if food.is_eaten(player_snake.head):
        food.change_location()
        fakefood.change_location()
        player_snake.add_segment()
        scoreboard.refresh()

    # Detect enemy collision with food
    if food.is_eaten(enemy_snake.head) or fakefood.is_eaten(enemy_snake.head):
        food.change_location()
        fakefood.change_location()
        enemy_snake.add_segment()

    # Detect player collision with fake food
    if fakefood.is_eaten(player_snake.head):
        player_snake.die(SNAKE_LENGTH)
        scoreboard.reset_score()

    # Detect collision with a wall
    if player_snake.is_wall_hit() and BORDER_MODE == 1:
        player_snake.die(SNAKE_LENGTH)
        scoreboard.reset_score()

    player_snake.loop_board()
    enemy_snake.loop_board()

    # Detect player collision with tail
    player_bite = player_snake.which_segment_is_bitten()
    if player_bite:
        if TAIL_MODE == 0:
            player_snake.eat_tail(player_bite)
        else:
            player_snake.die(SNAKE_LENGTH)
            scoreboard.reset_score()

window.exitonclick()
