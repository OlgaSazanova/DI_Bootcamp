import random
import json
#1 Description: In this exercise we will create a random sentence generator.
#  We will do this by asking the user how long the sentence should be and then printing the generated sentence.

# Create a function called get_words_from_file. 
# This function should read the file’s content and return the words as a collection.
#  What is the correct data type to store the words? List


def get_words_from_file(file_location):
    contents = ""
    with open(file_location, 'r') as file:
        contents = file.read()
    content_list = []
    content_list = contents.split("\n") 
    
    #print(content_list)
    return content_list




# Create another function called get_random_sentence which takes a single parameter called length.
# The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.the amount of words should be the value of the length parameter.
# Take the random words and create a sentence (using a python method), the sentence should be lower case.

def get_random_sentence(length : int) -> str:
    
    random_words = random.sample(content_list, length) 
    random_sentence = ' '.join(random_words)
    random_sentence = random_sentence.lower()
    return random_sentence


# Create a function called main which will:
# Print a message explaining what the program does.
# Ask the user how long they want the sentence to be. 
# Acceptable values are: an integer between 2 and 20.
#  Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.

def main():
    print(''' Hello! This is a random sentence generator. 
    You just should say how long (how many words)the sentence should be
    and then program will print the generated sentence''')

    global content_list
    length = input('How many words should be in the sentence? (write an integer between 2 and 20)  ')
    length = int(length)
    file_location = "sowpods.txt"
    content_list = get_words_from_file(file_location)


    try:

        if 2 <= length <= 20:
            print(f'Great! You chose {length}')
            output = get_random_sentence(length)
            print(output)
        else:
            raise ('The length must be between 2 and 20')
    except ValueError: 
        print('You provided incorrect data' )

if __name__ == "__main__":
    main()




#2 

sample_json = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# Access the nested “salary” key from the JSON-string above.

contents_dict = json.loads(sample_json)  # json.loads reads a json string
print(contents_dict)
salary= ''
salary = contents_dict['company']['employee']['payable']['salary']
print(salary)

# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
contents_dict['company']['employee']['birth_date'] = '1988-3-30'

# Save the dictionary as JSON to a file.

new_json= 'updated json'
with open(new_json, mode="w") as file:
    json.dump(contents_dict, file, indent=4)

print(json.dumps(contents_dict, indent=4)) 
