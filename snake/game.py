import snake
import food
from typing import (TypeVar, Optional)

ObsType = TypeVar("ObsType")


class Game:
    """
        Środowisko gry snake
        :argument width: szerokość planszy
        :argument height: wysokość planszy

        :parameter mode: soft_wall / hard_wall, przechodzenie przez ściany lub nie
        :var board: macierz przechowująca wszystkie elementy świata gry
        :var snake(Snake): obiekt przechowujący inforamcję o snaku i jego logikę
        :var fruit(Fruit): obiekt owocu, czyli celu snaka


        is_end(): sprawdzenie warunku końca gry
        update_board(): czyści planszę gry i ustawia na nowo wyszystkie elementy na planszy
        get_state(): zwraca planszę zapisaną jako int
        get_state_as_vector(): zwraca planszę jak wektor
        reset(): przywracanie stanu gry do początkowego stanu. Zwraca stan początkowy
    """
    def __init__(self, width, height):

        self.mode = "soft_wall"  # soft_wall / hard_wall
        self.score = 0

        self.width = width
        self.height = height

        self.observation_space = width * height
        self.action_space = 4

        self.board = []
        self.snake = None
        self.fruit = None

        self.null_state = 0

        self.reset()

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
        """Sprawdza warunek końca gry
        """
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
            self.board[elem[1]][elem[0]] = 1

        self.board[self.fruit.y][self.fruit.x] = 1

    def set_direction(self, action: int):
        """Ustawienie kierunku, w którą będzie się poruszał Snake na postwie przekazanej akcji"""
        if action is None:
            action = self.snake.direction
        new_direction = action

        #uniemożliwienie ruchu przeciwnego do aktualnego kierunku
        if (self.snake.direction == 0 and new_direction == 1) or (self.snake.direction == 1 and new_direction == 0):
            return
        elif (self.snake.direction == 2 and new_direction == 3) or (self.snake.direction == 3 and new_direction == 2):
            return
        else:
            self.snake.direction = new_direction

    def get_state(self):
        """
            :returns: board as int
        """
        flat_arr = [item for sublist in self.board for item in sublist]

        # Convert the flattened array into a binary number
        return int(''.join(map(str, flat_arr)), 2)

    def get_state_as_vector(self):
        """
        :returns: board as vector
        """
        flat_arr = [item for sublist in self.board for item in sublist]

        return flat_arr

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

        return new_state, reward, game_over

    def step_dqn(self, action):
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

        new_state = self.get_state_as_vector()

        return new_state, reward, game_over

    def reset(self, seed: Optional[int] = None):
        """Reset game
        Przywracanie stanu gry do początkowego stanu
        :returns: state of board
                """
        if seed is not None:
            self.seed = seed

        #reset all game objects
        self.board = [[0 for j in range(self.width)] for i in range(self.height)]
        self.snake = snake.Snake(self.width, self.height)
        self.fruit = food.Food(self.width, self.height, seed)

        self.update_board()
        self.null_state = 0

        self.score = 0

        return self.get_state_as_vector()

    def close(self):
        pass
