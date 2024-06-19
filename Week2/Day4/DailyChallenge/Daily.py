from collections import Counter
import string

import os
# First, we will analyze a simple string, like “A good book would sometimes cost as much as a good house.”

# Create a class called Text that takes a string as an argument and store the text in a attribute.

class Text:
    def __init__(self, text : str):
        self.text = text

# Implement the following methods:
# a method to return the frequency of a word in the text (assume words are separated by whitespace)
#  return None or a meaningful message.
    def freq_word(self, word):

        translator = str.maketrans('', '', string.punctuation)
        cleaned_text = self.text.translate(translator)
        words = cleaned_text.lower().split()
        frequency = words.count(word)

        if frequency == 0:
            return f'There is not word "{word}" in the string.'
        else:
            return f'The "{word}" appears {frequency} in the string.'  


# a method that returns the most common word in the text.
    def most_common(self):
        translator = str.maketrans('', '', string.punctuation)
        cleaned_text = self.text.translate(translator)
        words = cleaned_text.lower().split()
        character_counter = Counter(words)
        most_common_word, count = character_counter.most_common(1)[0]
        return f'The most common word is "{most_common_word}" which appears {count} times.'

# a method that returns a list of all the unique words in the text.  
    def unique_words(self):
        translator = str.maketrans('', '', string.punctuation)
        cleaned_text = self.text.translate(translator)
        words = cleaned_text.lower().split()
        unique_words_set = set(words)
        return list(unique_words_set)


our_text = 'A good book would sometimes cost as much as a good house.'
text_obj = Text(our_text)
   
        
word = "good"
print(text_obj.freq_word(word))

word2 = "house"
print(text_obj.freq_word(word2))

word3 = "something"
print(text_obj.freq_word(word3))

print(text_obj.most_common())

print(text_obj.unique_words())

# Part II
# Then, we will analyze a text coming from an external text file. Download the_stranger.txt file.
# Implement a classmethod that returns a Text instance but with a text file:

#     >>> Text.from_file('the_stranger.txt')
# Hint: You need to open and read the text from the text file.


 
#######################


class Text:
    def __init__(self, txt_str: str):
        self.txt_str = txt_str

    @classmethod
    def from_file(cls, file_name: str):
        try:
            with open(file_name, 'r') as file:
                text_file = file.read()
            return cls(text_file)
        except FileNotFoundError:
            print(f"Error: The file '{file_name}' was not found in the directory '{os.getcwd()}'.")
            print("Files in directory:", os.listdir())
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

# Try to create a Text instance from the file using raw string for the path
text2 = Text.from_file(r'C:\Users\olgak\Desktop\Developers Insitiute\DI_Bootcamp\Week2\Day4\DailyChallenge\the_stranger.txt')

# If the file was found and text2 is not None, print the first 50 characters
if text2:
    print(text2.txt_str[:50])
else:
    print("Text object creation failed.")
