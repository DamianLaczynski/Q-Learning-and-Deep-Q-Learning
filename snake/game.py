import time
import random
import snakeGame
import food
import display

class Game:
    board = []
    width = 0
    height = 0
    score = 0

    direction = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0 for j in range(height)] for i in range(width)]

    def updateBoard(self, snake, fruit):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j] = 0

        self.board[snake.x][snake.y] = 1
        self.board[fruit.x][fruit.y] = 1

    def getScore(self):
        return self.score

    def isColision(self, snake, fruit):
        if snake.x == fruit.x & snake.y == fruit.y:
            return True

    def isEnd(self, snake):
        if snake.isColision() == True:
            return True
        else:
            return False

    def start(self):
        game_over = False

        snake = snakeGame.SnakeClass(int(self.width / 2), int(self.height / 2), width=self.width, height=self.height)

        fruit = food.Food()

        fruit.randNewPosition(self.width, self.height)

        #main loop
        while not game_over:
            snake.move(self.direction)
            self.updateBoard(snake, fruit)
            display.display(self.board)
            if self.isColision(snake, fruit):
                fruit.randNewPosition(self.width, self.height)
                self.score += 1
            if self.isEnd(snake) == True:
                game_over = True
            time.sleep(1)
