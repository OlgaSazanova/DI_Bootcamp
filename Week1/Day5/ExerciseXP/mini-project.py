#build a playground as on the picture on the website

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
            if pixel==0:
                print(' ', end='')
            if pixel==1:
                print('*', end='')
            if pixel==2:
                print('|', end='')   
            if pixel==3:
                print('-', end='')
        
        print('')



# function for getting input from user. DOESN'T WORK!!!! It doesn't insert a user's sign to playground
# but playground changes itself - so we see that function takes a proper indexes

def user_input(player, user_row, user_column):

    global playground

    user_row = int(user_row)
    user_column = int(user_column)

    row_index = (user_row - 1) * 2 + 1
    col_index = (user_column - 1) * 4 + 4


    if 1 <= user_row <= 3 and 1 <= user_column <= 3:
        if playground[row_index][col_index] == 0:
            playground[row_index][col_index] = player
        else:
            print('Position already taken, choose another position')
    else:
        print('Your row or column number is wrong, enter numbers betwee 1 and 3.')


display_board(playground)
 



def check_win(playground):
    # check rows and columns
    for i in range(1, 6, 2):  
        if playground[i][4] == playground[i][8] == playground[i][12] != 0:
            return playground[i][4]

    for j in range(4, 13, 4): 
        if playground[1][j] == playground[3][j] == playground[5][j] != 0:
            return playground[1][j]

    # check diaganols
    if playground[1][4] == playground[3][8] == playground[5][12] != 0:
        return playground[1][4]

    if playground[1][12] == playground[3][8] == playground[5][4] != 0:
        return playground[1][12]

    return 0  



def play():
    playground = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 3, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    display_board(playground)
    
    list_of_possible_positions = [
    playground[1][4], playground[1][8], playground[1][12],
    playground[3][4], playground[3][8], playground[3][12],
    playground[5][4], playground[5][8], playground[5][12]
    ]

    player = input('Enter a player(X or O): ').upper()
    while player not in ['X', 'O']:
        player = input('Invalid input. Enter a player(X or O): ').upper()

    while True:
        user_row = input('Enter row (1-3): ')
        user_column = input('Enter column (1-3): ')

        if user_input(player, user_row, user_column, playground):
            display_board(playground)
            winner = check_win(playground)
            if winner:
                print(f'Player {winner} wins!')
                break
            elif all(position != 0 for position in list_of_possible_positions):
                print('It\'s a tie!')
                break

            player = 'O' if player == 'X' else 'X'  # Switch player for next turn
        else:
            continue


play()