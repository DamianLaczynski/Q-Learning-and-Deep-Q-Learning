import random


class Food:
    x = 0
    y = 0

    def randNewPosition(self, x_range, y_range):
        self.x = random.randrange(0, x_range, 1)
        self.y = random.randrange(0, y_range, 1)