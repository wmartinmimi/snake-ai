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

    invalid_pos = list(walls) + my_snake_body[1:]
    invalid_turns = []

    for turn in list(Turn):
        if my_snake.get_next_head(turn) in invalid_pos:
            invalid_turns.append(turn)
    
    (snake_x, snake_y) = my_snake.head
    (closest_food_x, closest_food_y) = list(food)[0]
    shortest_food_dist = 9999999999999

    print(f"Food: {closest_food_x}, {closest_food_y}")
    print(f"Snake: {snake_x}, {snake_y}")

    for (food_x, food_y) in list(food):
        dx = food_x - snake_x
        dy = snake_y - food_y
        dist = abs(dx) + abs(dy)
        print(f"dist: {dist}, shortest: {shortest_food_dist}")
        if dist < shortest_food_dist:
            shortest_food_dist = dist
            closest_food_x = food_x
            closest_food_y = food_y

    dx = closest_food_x - snake_x
    dy = snake_y - closest_food_y
    turn = Turn.STRAIGHT

    if abs(dx) >= abs(dy):
        if dx > 0:
            match my_snake_direction:
                case Direction.UP:
                    turn = Turn.RIGHT
                case Direction.DOWN:
                    turn = Turn.LEFT
                case Direction.LEFT:
                    turn = Turn.RIGHT
                case Direction.RIGHT:
                    turn = Turn.STRAIGHT
        elif dx < 0:
            match my_snake_direction:
                case Direction.UP:
                    turn = Turn.LEFT
                case Direction.DOWN:
                    turn = Turn.RIGHT
                case Direction.LEFT:
                    turn = Turn.STRAIGHT
                case Direction.RIGHT:
                    turn = Turn.LEFT
    else:
        if dy > 0:
            match my_snake_direction:
                case Direction.UP:
                    turn = Turn.STRAIGHT
                case Direction.DOWN:
                    turn = Turn.LEFT
                case Direction.LEFT:
                    turn = Turn.RIGHT
                case Direction.RIGHT:
                    turn = Turn.LEFT
        elif dy < 0:
            match my_snake_direction:
                case Direction.UP:
                    turn = Turn.LEFT
                case Direction.DOWN:
                    turn = Turn.STRAIGHT
                case Direction.LEFT:
                    turn = Turn.LEFT
                case Direction.RIGHT:
                    turn = Turn.RIGHT

    if turn in invalid_turns:
        for fix_turn in list(Turn):
            if fix_turn not in invalid_turns:
                turn = fix_turn
                break
        # if reach here, then dead anyways

    return turn

    # return random.choice(list(Turn))

    # ======================================
    # =       Try out some examples!       =
    # ======================================

    # from examples.dumbAI import dumbAI
    # return dumbAI(state)

    # from examples.smartAI import smartAI
    # return smartAI(state)
