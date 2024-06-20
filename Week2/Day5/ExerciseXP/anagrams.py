import anagram_checker

file_location = "sowpods.txt"

checker = anagram_checker.AnagramChecker(file_location)
def menu():

# Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.
    while True:       
        
        print('Anagram Checker \nThis program will ask you for a word and then will find all possible anagrams for that word.' )
        print('Word should be a valid English word')
        action= input('If you want to try a program - write "Y" \nIf you want to quit - write "q"  ') 

# If the user chooses to input a word, it must be accepted from the user’s keyboard input, and then be validated:
# Whitespace should be removed from the start and end of the user’s input. 
        
        if action == 'Y':
            word = input('Provide, please, any word in English: ').strip().upper()
            

# Only a single word is allowed. If the user typed more than one word, show an error message.

            if len(word.split()) > 1:
                raise ValueError ('Your entered more than one word')
            elif len(word.split()) == 1:

    # Only alphabetic characters are allowed. No numbers or special characters. 

                if word.isalpha():

                                        
                    if checker.is_valid_word(word):
                        output_list = checker.get_anagrams(word)
                        output_list_string = ', '.join(output_list) 
    # Once your code has decided that the user’s input is valid, it should find out the following: 
                        print(f'YOUR WORD: "{word}" \nthis is a valid English word. \nAnagrams for your word: {output_list_string}')

                    else:
                        raise ValueError('Your word is not valid.')
                else: 
                    raise ValueError('Your word is not valid.')

        elif action == 'q':
            print('Good bye!')
            break

        else:
            print('Please, write Y or q')
            continue


if __name__ == "__main__":
    menu()
    





