# Игровое поле (пример)
playground = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

def display_board(playground):
    for row in playground:
        for pixel in row:
            if pixel == 0:
                print(' ', end='')
            elif pixel == 1:
                print('*', end='')
            elif pixel == 2:
                print('|', end='')   
            elif pixel == 3:
                print('-', end='')
        print('')

def user_input(player, user_row, user_column):
    global playground

    user_row = int(user_row)
    user_column = int(user_column)

    # Вычисляем индексы строки и столбца в playground
    if user_row == 1:
        row_index = 1
    elif user_row == 2:
        row_index = 3
    elif user_row == 3:
        row_index = 5
    
    if user_column == 1:
        col_index = 6
    elif user_column == 2:
        col_index = 10
    elif user_column == 3:
        col_index = 14

    # Проверяем корректность введенных данных
    if 1 <= user_row <= 3 and 1 <= user_column <= 3:
        if playground[row_index][col_index] == 0:
            playground[row_index][col_index] = player
        else:
            print('Position already taken, choose another position')
    else:
        print('Your row or column number is wrong, enter numbers between 1 and 3.')

# Отображаем начальное состояние игрового поля
display_board(playground)

# Вводим игрока и координаты хода
player = input('Enter a player (X or O): ')
user_row = input('Enter row (1, 2 or 3): ')
user_column = input('Enter column (1, 2 or 3): ')

# Вызываем функцию для обработки хода игрока
user_input(player, user_row, user_column)

# Отображаем обновленное состояние игрового поля
display_board(playground)
