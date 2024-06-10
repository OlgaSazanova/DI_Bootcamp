# 1. Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.

user_number=input('Provide a number: ')
length=input('Provide a length: ')

user_number=int(user_number)
length=int(length)

new_list=[]
new_list.append(user_number)

number = user_number

while len(new_list) != length:
    number += user_number
    new_list.append(number)

print(new_list)

#2. Write a program that asks a string to the user,
#  and display a new string with any duplicate consecutive letters removed.

user_string=input('Write a string with any duplicate consecutive letters: ')
new_string= ''
for i in range(len(user_string)-1):
    if user_string[i] !=user_string[i+1]:  # compare the letter with the next letter

        new_string += user_string[i]  #to add letter to the new string

#to add last letter
new_string = new_string + user_string[-1]
print(new_string)