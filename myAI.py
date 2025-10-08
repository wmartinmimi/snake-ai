import random
from collections import deque
from snake.logic import GameState, Turn, Snake, Direction

"""
Your mission, should you choose to accept it, is to write the most cracked snake AI possible.

All the info you'll need to do this is in the GameState and Snake classes in snake/logic.py

Below is all of the data you'll need, and some small examples that you can uncomment and use if you want :)

"""


def myAI(state: GameState) -> Turn:

    # ======================================
    # =         Some Useful data.          =
    # ======================================

    grid_width: int = state.width
    grid_height: int = state.height
    # set of tuples (x, y)
    food: set = state.food
    walls: set = state.walls
    score: int = state.score
    my_snake: Snake = state.snake
    my_snake_direction: Direction = Direction(state.snake.direction)
    my_snake_body: list = list(state.snake.body)
    enemy_snakes = state.enemies

    # you may also find the get_next_head() method of the Snake class useful!
    # this tells you what position the snake's head will end up in for each of the moves
    # you can then check for collisions, food etc
    straight = my_snake.get_next_head(Turn.STRAIGHT)
    left = my_snake.get_next_head(Turn.LEFT)
    right = my_snake.get_next_head(Turn.RIGHT)

    # ======================================
    # =         Your Code Goes Here        =
    # ======================================

    (food_x, food_y) = list(food)[0]
    (snake_x, snake_y) = my_snake.head

    print(f"Food: {food_x}, {food_y}")
    print(f"Snake: {snake_x}, {snake_y}")

    dx = food_x - snake_x
    dy = snake_y - food_y

    if abs(dx) >= abs(dy):
        if dx > 0:
            match my_snake_direction:
                case Direction.UP:
                    return Turn.RIGHT
                case Direction.DOWN:
                    return Turn.LEFT
                case Direction.LEFT:
                    return Turn.RIGHT
                case Direction.RIGHT:
                    return Turn.STRAIGHT
        elif dx < 0:
            match my_snake_direction:
                case Direction.UP:
                    return Turn.LEFT
                case Direction.DOWN:
                    return Turn.RIGHT
                case Direction.LEFT:
                    return Turn.STRAIGHT
                case Direction.RIGHT:
                    return Turn.LEFT
    else:
        if dy > 0:
            match my_snake_direction:
                case Direction.UP:
                    return Turn.STRAIGHT
                case Direction.DOWN:
                    return Turn.LEFT
                case Direction.LEFT:
                    return Turn.RIGHT
                case Direction.RIGHT:
                    return Turn.LEFT
        elif dy < 0:
            match my_snake_direction:
                case Direction.UP:
                    return Turn.LEFT
                case Direction.DOWN:
                    return Turn.STRAIGHT
                case Direction.LEFT:
                    return Turn.LEFT
                case Direction.RIGHT:
                    return Turn.RIGHT

    return Turn.RIGHT

    # return random.choice(list(Turn))

    # ======================================
    # =       Try out some examples!       =
    # ======================================

    # from examples.dumbAI import dumbAI
    # return dumbAI(state)

    # from examples.smartAI import smartAI
    # return smartAI(state)
