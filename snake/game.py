import time
import snakeGame
import food
import display

class Game:
    board = []
    width = 0
    height = 0
    score = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0 for j in range(height)] for i in range(width)]
        self.snake = snakeGame.SnakeClass(int(self.width / 2), int(self.height / 2), width=self.width, height=self.height)
        self.fruit = food.Food(self.width, self.height)

    def updateBoard(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j] = 0

        #dodawanie wszystkich członów węża do tablicy
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
        self.snake.direction = action

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

        print(self.score)

        game_over = self.isEnd()

        return self.board, reward, game_over


