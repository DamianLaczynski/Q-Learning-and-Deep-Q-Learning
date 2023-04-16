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
    print('\n'*20) # prints 80 line breaks
    for i in range(game.width):
        for j in range(game.height):
            print(game.getBoard()[i][j], end=' ')

        print()
