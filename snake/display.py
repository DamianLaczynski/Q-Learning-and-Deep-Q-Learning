from os import system, name


# define our clear function
def clear():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')


def display(game):
    print('\n'*40)  # prints 80 line breaks
    print('|' + '-' * game.width + '|')
    for i in range(game.width):
        print('|', end='')
        for j in range(game.height):
            if game.getBoard()[i][j] == 0:
                print(' ', end='')
            else:
                if game.get_fruit().x == j and game.get_fruit().y == i:
                    print('O', end='')  # fruit
                elif game.get_snake().x == j and game.get_snake().y == i:
                    print('@', end='')  # head
                else:
                    print('#', end='')  # snake body
        print('|', end=' ')
        print()
    print('|' + '-' * game.width + '|')

    print()
    print(game.getScore())
