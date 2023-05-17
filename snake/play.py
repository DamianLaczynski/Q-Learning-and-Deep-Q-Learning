import game
import display as ds
import inputController
import time


def main():
    my_game = game.Game(20, 6)
    ds.display(my_game)
    while(True):
        action = inputController.get_input()
        if action == -1:
            return 0
        my_game.step(action)
        if my_game.is_end() == True:
            return 0
        ds.display(my_game)
        time.sleep(0.1)

if __name__ == "__main__":
    main()