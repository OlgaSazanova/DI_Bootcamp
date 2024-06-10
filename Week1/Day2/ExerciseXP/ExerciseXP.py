#1. 
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.

my_fav_numbers={3, 37, 7, 137, 88}
my_fav_numbers.add(4)
my_fav_numbers.add(5)
print('My numbers with two new:', my_fav_numbers)

# Remove the last number.

my_fav_numbers=list(my_fav_numbers)
print('Now my numbers are in the list:', my_fav_numbers)
my_fav_numbers= my_fav_numbers[:-1]
print('Last number was removed:', my_fav_numbers)

# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
my_fav_numbers=set(my_fav_numbers)
friend_fav_numbers={1, 2, 3, 4}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print('Our numbers:', our_fav_numbers)

#2 
#Given a tuple which value is integers, is it possible to add more integers to the tuple?

# Yes, it's possible if cast a tuple to a list and then cast back to a tuple
# for example:
tuple_a= (3, 89, 43)
list_a=list(tuple_a)
print(list_a)
print(type(list_a))
list_a.extend([6, 100])
print(list_a)
tuple_a=tuple(list_a)
print(tuple_a)

#3

# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove('Banana')
print(basket)

# Remove “Blueberries” from the list.
basket.pop(-1)
print(basket)

# Add “Kiwi” to the end of the list.

basket.append('Kiwi')
print(basket)

# Add “Apples” to the beginning of the list.

basket.insert(0, 'Apples')
print(basket)

# Count how many apples are in the basket.

print(len(basket))

# Empty the basket.
# Print(basket)
basket.clear()
print(basket)


#4 Recap – What is a float? What is the difference between an integer and a float?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
# Can you think of another way to generate a sequence of floats?

#create list of integers
list_int=[] 

for num in range(2,6):
    list_int.append(num)

print(list_int)

# create list of floats
list_float=[] 

for n in list_int:
    n_float= n-0.5
    list_float.append(n_float)
print(list_float)

# our final list
two_lists= sorted( list_int + list_float) 
print(two_lists) 


#5  Use a for loop to print all numbers from 1 to 20, inclusive.


for k in range(1,20+1):
    print(k)

#Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.
list_numbers = []
for t in range(1,20+1):
    list_numbers.append(t)

for i, value in enumerate(list_numbers):
    if i % 2 == 0:
        print(value)

#6. Write a while loop that will continuously ask the user for their name,
#  unless the input is equal to your name.

my_name= 'Olga'
your_name = ''

while your_name != my_name:
    your_name=input('Please, write your name: ')
    continue

print('Our names are same:', my_name, 'and', your_name)

#7. Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".



user_fruits= input('''Please, write your favorite fruit(s) (one or several).
                    Separate the fruits with a single space, eg. "apple mango cherry"''')

# Store the favorite fruit(s) in a list (convert the string of words into a list of words).

user_fruits=user_fruits.split(' ')
print(user_fruits)

# Now that we have a list of fruits, ask the user to input a name of any fruit.
one_fruit= input('Write a name of any fruit ')

# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.
if one_fruit in user_fruits:
    print('You chose one of your favorite fruits! Enjoy!')
else:
    print('You chose a new fruit. I hope you enjoy')


#8  Write a loop that asks a user to enter a series of pizza toppings, 
# when the user inputs ‘quit’ stop asking for toppings.
#As they enter each topping, print a message saying you’ll add that topping to their pizza.
#Upon exiting the loop print all the toppings on the pizza pie 
# and what the total price is (10 + 2.5 for each topping).

toppings = []

while True:
    user_topping= input('What topping do you want? For stop to answer -  write "quit" ')
    if user_topping == 'quit':
        print('We going to add to your pizza:', toppings)
        price= 10+ len(toppings)*2.5
        print('Total price:', price)
        break 
    else:
        toppings.append(user_topping)




#9 A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Ask a family the age of each person who wants a ticket.


viewers_age = input('Please, provide age of viewers. Write it using a comma ')
viewers_age=list(viewers_age.split(','))
ages_num = []
for i in viewers_age:
    ages_num.append(int(i))

print(ages_num)

# Store the total cost of all the family’s tickets and print it out.
total = 0
for age in ages_num:
    if age > 12:
        total += 15
    elif 8<= age <=12:
        total += 10
    elif age<8:
        total += 0
        
print('The total price:', total)


# A group of teenagers are coming to your movie theater and want to watch a movie
#  that is restricted for people between the ages of 16 and 21.



names_teens=input('Please, provide your name. Use comma for separating ')
names_teens=list(names_teens.split(', '))

# Given a list of names, write a program that asks teenager for their age,
#  if they are not permitted to watch the movie, remove them from the list.
final_list = []
for name in names_teens:
    age_teen=input(f'{name}, write your age ')
    age_teen= int(age_teen)
    if 16 <= age_teen <= 21:
        final_list.append(name)
# At the end, print the final list.
print('You are permitted to watch a movie:', final_list)



#10
#Using the list below :

# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich",
#  "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# The deli has run out of pastrami, use a while loop to remove all occurrences of “Pastrami sandwich” 
# from sandwich_orders.

sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich",
 "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")

# We need to prepare the orders of the clients:
# Create an empty list called finished_sandwiches.
finished_sandwiches = []

# One by one, remove each sandwich from the sandwich_orders while adding them to the finished_sandwiches list.
while sandwich_orders != []:
    for sandwich in sandwich_orders:
        finished_sandwiches.append(sandwich)
        sandwich_orders.remove(sandwich)

# After all the sandwiches have been made, print a message listing each sandwich that was made, such as:
# I made your tuna sandwich
# I made your avocado sandwich
# I made your egg sandwich
# I made your chicken sandwich
for sandwich in finished_sandwiches:
    print('I made your ', sandwich)






    