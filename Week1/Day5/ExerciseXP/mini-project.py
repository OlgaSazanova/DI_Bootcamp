#build a playground


# = ' '
# 1= *
#2 =|
# 3 = -
playground =[
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

display_board(playground)

player = input('Enter a player( X or O) ')
user_row = input('Enter row: ')
user_column= input('Enter column ')


def player_input(player, user_row, user_column):


    # if user_row or user_column not in [1, 2, 3]:
    #     print('You are numbers wrong')


    
    for row in playground:
        for pixel in row:
            if user_row == 1 and user_column == 1 and playground[1][3] == 0:
                playground[1][3] == player
            elif  user_row == 1 and user_column == 2 and playground[1][8] == 0:
                playground[1][8] == player    
            elif user_row == 1 and user_column == 3 and playground[1][13] == 0:
                playground[1][13] == player
            elif user_row == 2 and user_column == 1 and playground[3][3] == 0:
                playground[3][3] == player
            elif user_row == 2 and user_column == 2 and playground[3][8] == 0:
                playground[3][8] == player
            elif user_row == 2 and user_column == 3 and playground[3][13] == 0:
                playground[1][3] == player
            elif user_row == 3 and user_column == 1 and playground[5][3] == 0:
                playground[5][3] == player
            elif user_row == 3 and user_column == 2 and playground[5][8] == 0:
                playground[5][8] == player
            elif user_row == 3 and user_column == 3 and playground[5][13] == 0:
                playground[5][13] == player
    print(playground)






# player_input(player) – To get the position from the player.
# check_win() – To check whether there is a winner or not.
# play() – The main function, which calls all the functions created above.