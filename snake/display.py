from os import system, name


# define our clear function
def clear():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')


def display(board):
    print('\n'*20) # prints 80 line breaks
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end='')

        print()
