def display(game):
    print('\n'*40)  # prints 40 line breaks

    print(game.get_score())
    print('|' + '-' * game.width + '|')
    for i in range(game.height):
        print('|', end='')
        for j in range(game.width):
            if game.get_board()[i][j] == 0:
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

