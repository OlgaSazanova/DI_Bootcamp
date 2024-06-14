#1
# Write a program that accepts a comma separated sequence of words as input 
# and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension
# Example:

# Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be: bag,hello,without,world


user_words = input('Provide, please, a comma separated sequence of words: ')


output = [word for word in user_words.split(sep=',')]

print(','.join(sorted(output)))

#2 
# Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word.
# Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).
# Examples

# longest_word("Margaret's toy is a pretty doll.") ➞ "Margaret's"

# longest_word("A thing of beauty is a joy forever.") ➞ "forever."

# longest_word("Forgetfulness is by all means powerless!") ➞ "Forgetfulness"




def longest_word(string):
    split_string= string.split(sep=' ')
    output_word =''
    for word in split_string:
        if len(output_word) < len(word):
            output_word = word
    return output_word

user_string= input('Write a sentence: ')
answer = longest_word(user_string)
print(f'The longest word: {answer}')


