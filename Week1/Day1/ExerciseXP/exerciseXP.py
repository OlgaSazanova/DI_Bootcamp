#1. Print the following output in one line of code:

#Hello world
#Hello world
#Hello world
#Hello world

print('Hello world\nHello world\nHello world\nHello world')

#2. Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).


print((99**3)*8)

#3. Predict the output of the following code snippets:
#>>> 5 < 3              # False
#>>> 3 == 3             # True
#>>> 3 == "3"           # False
#>>> "3" > 3            # False
#>>> "Hello" == "hello" # False

#4. Create a variable called computer_brand which value is the brand name of your computer.
# Using the computer_brand variable print a sentence that 
# states the following: "I have a <computer_brand> compute

computer_brand = 'HP'
print(f'I have a {computer_brand} computer')

#5. Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. 
# The sentence must contain all the variables created in parts 1, 2 and 3.
# Have your code print the info message.
# Run your code

name = 'Olga'
age = 36
shoe_size = 37

info = f"My name is {name}, I'm {age} years old, my  shoe size is {shoe_size}"
print(info)

# 6 Create two variables, a and b.
# Each variable value should be a number.
# If a is bigger then b, have your code print Hello World.

a = 54
b = 9

if a>b:
    print('Hello World')
else:
    print('a is not bigger then b')


# 7. Write code that asks the user for a number and determines whether this number is odd or even.


user_number = input('Please, write a number: ')

if (user_number % 2 == 0):
    print('Your number is even')
else:
    print('Your number is odd')


# 8 Write code that asks the user for their name and determines whether or not you have the same name,
#  print out a funny message based on the outcome.

your_name= input('Provide your name, please: ')
my_name = 'Olga'
if your_name != my_name:
    print(f'Nice to meet you, {your_name}')
if your_name == my_name: 
    print(f'Wow, {your_name}, we have the same name!')

#9 Write code that will ask the user for their height in centimeters.
# If they are over 145cm print a message that states they are tall enough to ride.
# If they are not tall enough print a message that says they need to grow some more to ride.

user_height= input(f'Provide, please, your height in centimeters: ')
user_height = int(user_height)
if user_height > 145:
    print('You are tall enough to ride')
else:
    print('You need to grow some more to ride')
