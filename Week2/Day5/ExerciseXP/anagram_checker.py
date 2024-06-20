
file_location = "sowpods.txt"

class AnagramChecker:
    #__init__ - should load the word list file (text file) into a variable, 
    # so that it can be searched later on in the code.
    def __init__(self, file_location: str) -> None:
        self.file_location = file_location
        contents = ""
        with open(file_location, 'r') as file:
            contents = file.read()
        content_list = []
        self.content_list = contents.split("\n") 
    
        #print(content_list)
        #return content_list
    
#is_valid_word(word) – should check if the given word (ie. the word of the user) is a valid word.

    def is_valid_word(self, word : str) -> bool: 
        self.word = word
        if word in self.content_list:
               return True
        else:
               return False
              

#get_anagrams(word) – should find all anagrams for the given word. 
    def get_anagrams(self, word : str) -> list:
        word_sorted = sorted(word)
        list_of_anagrams = []


        for i in self.content_list:
            if word_sorted == sorted(i) and word != i:
                list_of_anagrams.append(i)

        return list_of_anagrams










