import random
from collections import deque
from snake.logic import GameState, Turn, Snake, Direction
from smartAI import smartAI as enemyAI
from src.game_clone.patch import SnakeGame as PatchedSnakeGame

"""
Your mission, should you choose to accept it, is to write the most cracked snake AI possible.

All the info you'll need to do this is in the GameState and Snake classes in snake/logic.py

Below is all of the data you'll need, and some small examples that you can uncomment and use if you want :)

"""


def simulateTurn(game: PatchedSnakeGame, food) -> PatchedSnakeGame | None:
    # moves all the snakes one by one
    # note that the player's snake is at index 0
    for i in range(len(game.snakes)):
        if game.snakes[i].isAlive:
            state = game.getGameState(i)
            turn = internalAI(state, food) if i == 0 else enemyAI(state)
            game.move_snake(i, turn)
    return game


def lookAhead(state: GameState) -> Turn:
    original_length = len(state.snake.body_set)
    for nth_food in range(len(set(state.food))):
        game = PatchedSnakeGame(state)
        food = nthClosestApple(state, nth_food)
        for _ in range(1000):
            game = simulateTurn(game, food)
            if game is None:
                break
            if original_length < len(game.snakes[0].body_set):
                return internalAI(state, food)


    invalid_pos = list(state.walls) + list(state.snake.body)[1:]
    for enemy in state.enemies:
        invalid_pos += list(enemy.body)
    invalid_turns = []

    for turn in list(Turn):
        if state.snake.get_next_head(turn) in invalid_pos:
            invalid_turns.append(turn)

    if turn in invalid_turns:
        for fix_turn in list(Turn):
            if fix_turn not in invalid_turns:
                turn = fix_turn
                break
        # if reach here, then dead anyways


    print("messed up")
    return Turn.STRAIGHT


def nthClosestApple(state: GameState, n: int) -> (int, int):
    (snake_x, snake_y) = state.snake.head
    (closest_food_x, closest_food_y) = list(state.food)[0]
    shortest_food_dist = [99999999]
    closest_food = []

    print(f"Food: {closest_food_x}, {closest_food_y}")
    print(f"Snake: {snake_x}, {snake_y}")

    for (food_x, food_y) in list(state.food):
        print(5)
        dx = food_x - snake_x
        dy = snake_y - food_y
        dist = abs(dx) + abs(dy)
        print(f"dist: {dist}, shortest: {shortest_food_dist}")
        for idx, shortest in enumerate(shortest_food_dist):
            print(6)
            if dist < shortest:
                print(7)
                shortest_food_dist.insert(idx, dist)
                closest_food.insert(idx, (food_x, food_y))
                break

    return closest_food[n]


def internalAI(state: GameState, apple: (int, int)) -> Turn:
    """
    return turn and if successfully ate apple
    """
    food: set = state.food
    walls: set = state.walls
    my_snake: Snake = state.snake
    my_snake_direction: Direction = Direction(state.snake.direction)
    my_snake_body: list = list(state.snake.body)

    invalid_pos = list(walls) + my_snake_body[1:]
    for enemy in state.enemies:
        invalid_pos += list(enemy.body)
    invalid_turns = []

    for turn in list(Turn):
        if my_snake.get_next_head(turn) in invalid_pos:
            invalid_turns.append(turn)
    
    (snake_x, snake_y) = my_snake.head
    (closest_food_x, closest_food_y) = list(food)[0]
    shortest_food_dist = 9999999999999

    print(f"Food: {closest_food_x}, {closest_food_y}")
    print(f"Snake: {snake_x}, {snake_y}")

    (food_x, food_y) = apple
    dx = food_x - snake_x
    dy = snake_y - food_y
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

def myAI(state: GameState) -> Turn:
    """
    The main entry point for AI program
    """

    return lookAhead(state)

