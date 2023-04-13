class SnakeClass:
    x = 0
    y = 0

    board_w = 0
    board_h = 0

    def __init__(self, start_x, start_y, width, height):
        self.x = start_x
        self.y = start_y
        self.board_w = width
        self.board_h = height

    def isColision(self):
        #TODO dopisać zapisywanie pozycji ogona
        return False

    def move(self, direction):
        #move top
        if direction == 1:
            self.y -= 1
            if self.y < 0:
                self.y = self.board_h - 1
        #move bottom
        elif direction == 2:
            self.y += 1
            if self.y >= self.board_h:
                self.y = 0
        #move left
        elif direction == 3:
            self.x -= 1
            if self.x < 0:
                self.x = self.board_w - 1
        #move right
        elif direction == 4:
            self.x += 1
            if self.x >= self.board_w:
                self.x = 0
