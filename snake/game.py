import time
import snakeGame
import food
import display

class Game:
    board = []
    width = 0
    height = 0
    score = 0

    direction = 1

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0 for j in range(height)] for i in range(width)]

    def updateBoard(self, snake, fruit):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j] = 0

        #dodawanie wszystkich członów węża do tablicy
        for elem in snake.snakeList:
            self.board[elem[1]][elem[0]] = 1

        self.board[fruit.y][fruit.x] = 1

    def getScore(self):
        return self.score

    def setDirection(self, direction):
        self.direction = direction

    def isColision(self, snake, fruit):
        if snake.x == fruit.x and snake.y == fruit.y:
            return True
        else:
            return False

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
            # sterowanie snake-m
            snake.move(self.direction)
            if self.isColision(snake, fruit):
                fruit.randNewPosition(self.width, self.height)
                snake.addNewElem()
                self.score += 1

            self.updateBoard(snake, fruit)
            #wyświetlanie planszy w konsoli
            display.display(self.board)
            print(self.score)

            # zjedzenie owocu i zdobycie punktu

            # jeśli snake połknął ogon to koniec gry
            if self.isEnd(snake) == True:
                game_over = True
            time.sleep(1)
