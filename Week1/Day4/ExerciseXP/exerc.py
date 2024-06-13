#1 
# Write a function called display_message() that prints one sentence telling everyone 
# what you are learning in this course.
# Call the function, and make sure the message displays correctly.

def display_message():
    print('I learn Python')

display_message()

#2
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.

def favorite_book(title):
    return f"One of my favorite books is {title}"

print(favorite_book('Some'))

#3
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.

def describe_city(city, country = 'Israel'):
    
    print(f'{city} is in {country}')

describe_city('Akko')

# #4
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100. Use the random module.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.


import random

def two_numbers(num):
    second_num= random.randint(1,100)
    if num == second_num:
        print('wow! Succes!!!')
    else:
        print(f'Fail:(   The numbers were: {num} and {second_num}')

two_numbers(100)


#5
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, 
# such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().

def make_shirt(size, text_message):
    print(f"The size of the shirt is {size} and the text is {text_message}")

make_shirt(42, 'Eaaaat')



# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# Call the function, in order to make a large shirt with the default message

def make_shirt(size= 'Large', text_message= 'I love Python' ):
    print(f"The size of the shirt is {size} and the text is {text_message}")

make_shirt()


# Make medium shirt with the default message

make_shirt(size='Medium') 

# Make a shirt of any size with a different message.

make_shirt(size= 'Small', text_message= 'I love DI' )


# 6
# Using this list of magician’s names

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# Create a function called show_magicians(), which prints the name of each magician in the list.

def show_magicians(names):
    for name in names:
        print(name)

  

show_magicians(magician_names)
# Write a function called make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.


       
def make_great(magician_names):
    for i, name in enumerate(magician_names):
        magician_names[i] = f'the Great {name}'
make_great(magician_names)
    

show_magicians(magician_names)


# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.


#7 
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.

def get_random_temp():
    return random.randint(-10, 40)


print(get_random_temp())

# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”
# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40

def main():
    temp = get_random_temp()
    print(f'The temperature right now is {temp} degrees Celsius.')
    
    if temp <0:
        print('Brrr, that’s freezing! Wear some extra layers today')
    elif 0<= temp < 16:
        print('Quite chilly! Don’t forget your coat')
    elif 16<= temp < 23:
        print('Nice wheather,just have a jacket')
    elif 24<= temp < 32:
        print('Great weather! Enjoy the summer')
    elif 32<= temp < 40:
        print('So hot! Stay at home!')

        
main()



# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season,
#  eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly.
#  Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().

season = input('Choose a season: summer, autumn, winter or spring:  ')
def get_random_temp2(season):
    if season == 'winter':
        return random.randint(-10, 0)
    elif season == 'spring':
        return random.randint(1, 15)
    elif season== 'summer':
        return random.randint(25, 40)
    elif season == 'autumn':
        return random.randint(16, 26)
    
def main2():
    temp = get_random_temp2(season)
    print(f'The temperature right now is {temp} degrees Celsius.')
    
    if temp <0:
        print('Brrr, that’s freezing! Wear some extra layers today')
    elif 0<= temp < 16:
        print('Quite chilly! Don’t forget your coat')
    elif 16<= temp < 23:
        print('Nice wheather,just have a jacket')
    elif 24<= temp < 32:
        print('Great weather! Enjoy the summer')
    elif 32<= temp < 40:
        print('So hot! Stay at home!')

        
main2()



#8 
# This project allows users to take a quiz to test their Star Wars knowledge.
# The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

# Here is an array of dictionaries, containing those questions and answers

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]


# Create a function that asks the questions to the user, and check his answers. 
correct_answers=0
incorrect_unswers = 0
wrong_answers = []
for topic in data:
    user_answer= input(topic['question']+ ' ')
    if user_answer== topic['answer']:
        print("That's right")
        correct_answers +=1
    elif user_answer != topic['answer']:
        print("That's wrong")
        incorrect_unswers +=1
        wrong_answers.append(user_answer)


print(f'Your wrong answers are: {wrong_answers}')
print(f'You answered correct to {correct_answers} questions')
print(f'You answered incorrect to {incorrect_answers} questions')
    # Track the number of correct, incorrect answers. Create a list of wrong_answers
# Create a function that informs the user of his number of correct/incorrect answers.

