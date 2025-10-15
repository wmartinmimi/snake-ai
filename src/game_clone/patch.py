
from src.game_clone.logic import SnakeGame as ClonedSnakeGame
from snake.logic import GameState

class SnakeGame(ClonedSnakeGame):
    def __init__(self, state: GameState):
        self.setGameState(state)

    # returns a game state from the perspective of a give snake
    # patch: assume self idx is 0
    def getGameState(self, idx):
        return GameState(
            width=self.width,
            height=self.height,
            snake=self.snakes[idx],
            enemies=[
                s for s in self.snakes if s != self.snakes[0] and s.isAlive
            ],
            food=self.food,
            walls=self.walls,
            score=self.snakes[idx].score,
        )

    # patch add function to clone game
    def setGameState(self, state: GameState):
        import copy
        state = copy.deepcopy(state)
        self.width = state.width
        self.height = state.height
        # patch: set self to always be idx 0
        self.snakes = [state.snake] + state.enemies
        self.food = state.food
        self.walls = state.walls
        self.game_over = False
        self.num_enemies = len(state.enemies)
        self.num_food = len(state.food)
        self.max_moves = 64
        self.moves = 0
        self.invalid_wall_cache = set() # not correct, as cache is not shared with game
        


