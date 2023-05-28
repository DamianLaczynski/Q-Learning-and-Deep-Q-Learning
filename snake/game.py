import snake
import food


def vect2d_to_int(arr, base):
    result = 0
    n = 1
    for a in reversed(range(0, len(arr))):
        for b in reversed(range(0, len(arr[a]))):
            result += n * arr[a][b]
            n *= base
    return result


class Game:


    def __init__(self, width, height):

        self.mode = "soft_wall"  # soft_wall / hard_wall
        self.score = 0

        self.width = width
        self.height = height

        self.board = [[0 for j in range(width)] for i in range(height)]
        self.snake = snake.Snake(self.width, self.height)
        self.fruit = food.Food(self.width, self.height)

        self.update_board()
        self.null_state = 0  # a state that never happens in the environment

    def get_board(self):
        return self.board

    def get_score(self):
        return self.score

    def get_fruit(self):
        return self.fruit

    def get_snake(self):
        return self.snake

    def set_direction(self, direction):
        self.snake.direction = direction

    def is_end(self):
        if self.snake.is_colision():
            return True
        else:
            return False

    def update_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board[i][j] = 0

        # dodawanie wszystkich członów węża do tablicy
        for elem in self.snake.snakeList:
            self.board[elem[1]][elem[0]] = 2

        self.board[self.snake.y][self.snake.x] = 3

        self.board[self.fruit.y][self.fruit.x] = 1

    def set_direction(self, action):
        if action == None:
            action = self.snake.direction
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
        return vect2d_to_int(flat_arr, 4)

    def is_food_in_snake(self):
        for elem in self.snake.snakeList:
            if elem[0] == self.fruit.x and elem[1] == self.fruit.y:
                return True
        return False

    def step(self, action):
        self.set_direction(action)

        hit_wall = self.snake.move()

        if hit_wall and self.mode == "hard_wall":
            return self.null_state, 0, True

        reward = 0

        if self.fruit.is_colision(self.snake.x, self.snake.y):
            self.fruit.rand_new_position()
            while self.is_food_in_snake():
                self.fruit.rand_new_position()
            self.snake.add_new_element()
            self.score += 1
            reward = 1

        self.update_board()

        game_over = self.is_end()

        new_state = self.get_state()

        # still don't know if we should use all rewards gathered to this point (self.score) or just reward that we earned at this moment
        return new_state, reward, game_over
        # return new_state, self.score, game_over
