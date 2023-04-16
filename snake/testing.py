import time

from snake import display
from snake.game import Game
import numpy as np

new_game = Game(5, 5)

game_over = False

while not game_over:
    _, _, game_over = new_game.step(np.random.choice([0,1,2,3]))
    display.display(new_game)
    time.sleep(1)
