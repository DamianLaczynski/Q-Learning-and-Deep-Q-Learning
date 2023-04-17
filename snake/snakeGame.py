class SnakeClass:
    x = 0
    y = 0

    board_w = 0
    board_h = 0

    lastRemovedElem = []

    direction = 1

    def __init__(self, start_x, start_y, width, height):
        self.x = start_x
        self.y = start_y
        self.board_w = width
        self.board_h = height
        self.snakeElem = []
        self.snakeElem.append(self.x)
        self.snakeElem.append(self.y + 1)
        self.snakeList = []
        self.snakeList.append(self.snakeElem)
        self.snakeHead = []
        self.snakeHead.append(self.x)
        self.snakeHead.append(self.y)
        self.snakeList.append(self.snakeHead)

    def isColision(self):
        for p in self.snakeList[:-1]:
            if p == [self.x, self.y]:
                return True
        return False

    def addNewElem(self):
        self.snakeList.insert(0, self.lastRemovedElem)

    def print_direction(self):
        if self.direction == 0:
            print("UP")
        elif self.direction == 1:
            print("DOWN")
        elif self.direction == 2:
            print("LEFT")
        else:
            print("RIGHT")

    def move(self):

        # direction == 0 -> don't change direction

        hit_wall = False

        # UP
        if self.direction == 0:
            self.y -= 1
            if self.y < 0:
                hit_wall = True
                self.y = self.board_h - 1
        # DOWN
        elif self.direction == 1:
            self.y += 1
            if self.y >= self.board_h:
                hit_wall = True
                self.y = 0
        # LEFT
        elif self.direction == 2:
            self.x -= 1
            if self.x < 0:
                hit_wall = True
                self.x = self.board_w - 1
        # RIGHT
        elif self.direction == 3:
            self.x += 1
            if self.x >= self.board_w:
                hit_wall = True
                self.x = 0

        self.snakeList.append([self.x, self.y])
        if len(self.snakeList) > 1:
            self.lastRemovedElem = self.snakeList[0]
            del self.snakeList[0]

        return hit_wall
