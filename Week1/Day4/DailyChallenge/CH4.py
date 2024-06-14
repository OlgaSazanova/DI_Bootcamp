# # Given a “Matrix” string:

#     7ii
#     Tsx
#     h%?
#     i #
#     sM 
#     $a 
#     #t%
#     ^r!

matrix= [
    [7, 'i', 'i'],
    ['T', 's', 'x'],
    ['h', '%', '?'],
    ['i', ' ', '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['^', 'r', '!']  
     ]

# To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column, 
# selecting only the alpha characters and connecting them. 
# so we transpose a matrix to be able to go through it like Neo did.
matrix_transp= [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
   

]

for i in range(len(matrix)):
    for k in range(len(matrix[0])):
        matrix_transp[k][i] = matrix[i][k]


# Then he replaces every group of symbols between two alpha characters by a space.
output_string= ''
for row in matrix_transp:

    for symb in row:
        if str(symb).isalpha():
            output_string += symb
        else:
            output_string += ' '

print(output_string)


