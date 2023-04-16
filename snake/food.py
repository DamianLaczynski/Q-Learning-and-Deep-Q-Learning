import random
import snakeGame


class Food:
    x = 0
    y = 0
    value = 2

    def __init__(self, width, height):
        self.randNewPosition(width, height)

    def randNewPosition(self, x_range, y_range):
        self.x = random.randrange(0, x_range, 1)
        self.y = random.randrange(0, y_range, 1)


