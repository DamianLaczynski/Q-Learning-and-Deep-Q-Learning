import random


class Food:
    x = 0
    y = 0
    board_w = 0
    board_h = 0
    value = 2

    def __init__(self, width, height, seed: int = None):
        self.board_w = width
        self.board_h = height
        self.rand_new_position()
        if seed is not None:
            random.seed(seed)

    def rand_new_position(self):
        self.x = random.randrange(0, self.board_w, 1)
        self.y = random.randrange(0, self.board_h, 1)

    def is_colision(self, x, y):
        if x == self.x and y == self.y:
            return True
        else:
            return False
