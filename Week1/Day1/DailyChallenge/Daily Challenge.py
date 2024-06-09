#1. Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.
# If it’s 10 characters, print a message which states “perfect string” and continue the exercise.


user_string = input('Please, write a string. The string must be 10 characters long. ')
print(user_string)

count_char = 0
for char in user_string:
    count_char += 1

print(count_char)

if count_char < 10:
    print ('string not long enough')
elif count_char >10:
    print('string too long')
elif count_char == 10:
    print('perfect string')


#Then, print the first and last characters of the given text.

print(user_string)
print(f'The first character: {user_string[0]}, the last character: {user_string[-1]}')

#Using a for loop, construct the string character by character: 
# Print the first character, then the second, then the third, until the full string is printed.

in_lines = ''

for char in user_string:
    in_lines += char
    print(in_lines)
