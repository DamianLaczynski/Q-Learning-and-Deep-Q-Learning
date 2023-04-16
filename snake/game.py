import time
import snakeGame
import food
import display


class Game:
    def __init__(self, width, height):
        self.score = 0
        self.width = width
        self.height = height
        self.board = [[0 for j in range(height)] for i in range(width)]
        self.snake = snakeGame.SnakeClass(int(self.width / 2), int(self.height / 2), width=self.width,
                                          height=self.height)
        self.fruit = food.Food(self.width, self.height)
        self.updateBoard()

    def updateBoard(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j] = 0

        # dodawanie wszystkich członów węża do tablicy
        for elem in self.snake.snakeList:
            self.board[elem[1]][elem[0]] = 1

        self.board[self.fruit.y][self.fruit.x] = 1

    def getBoard(self):
        return self.board

    def getScore(self):
        return self.score

    def setDirection(self, direction):
        self.snake.direction = direction

    def isColision(self):
        if self.snake.x == self.fruit.x and self.snake.y == self.fruit.y:
            return True
        else:
            return False

    def isEnd(self):
        if self.snake.isColision():
            return True
        else:
            return False

    def do_action(self, action):
        new_direction = action
        if (self.snake.direction == 0 and new_direction == 1) or (self.snake.direction == 1 and new_direction == 0):
            return
        elif (self.snake.direction == 2 and new_direction == 3) or (self.snake.direction == 3 and new_direction == 2):
            return
        else:
            self.snake.direction = new_direction

    def get_state(self):
        flat_arr = [item for sublist in self.board for item in sublist]

        # Convert the flattened array into a binary number
        return int(''.join(map(str, flat_arr)), 2)

    def step(self, action):
        self.do_action(action)

        self.snake.move()

        reward = 0

        if self.isColision():
            self.fruit.randNewPosition(self.width, self.height)
            self.snake.addNewElem()
            self.score += 1
            reward = 1

        self.updateBoard()

        game_over = self.isEnd()

        new_state = self.get_state()

        # still don't know if we should use all rewards gathered to this point (self.score) or just reward that we
        # earned at this moment
        return new_state, reward, game_over
        # return new_state, self.score, game_over
