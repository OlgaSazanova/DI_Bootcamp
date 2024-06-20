import random

class Game:
    
    def __init__(self) -> None:
        pass


# Ask the user to select an item (rock/paper/scissors). 
# Keep asking until the user has selected one of the items – use data validation and looping.
# Return the item at the end of the function.

    def get_user_item(self):
        
        while True: 
            user_item = input('Choose: rock/paper/scissors (enter "r",  "p" or  "s"): ').strip().lower()
        
            if user_item in  ['r', 'p', 's']:
                return user_item
            
            else:
                print('Invalid choice. Please, enter "r",  "p" or  "s"')         


# get_computer_item(self) – Select rock/paper/scissors at random for the computer. 
# Return the item at the end of the function. Use python’s random.choice() function (read about it online).
    def get_computer_item(self):
        return random.choice(['r', 'p', 's'])
       

# get_game_result(self, user_item, computer_item) – Determine the result of the game.

    
    def get_game_result(self, user_item, computer_item):
        # user_item – the user’s chosen item (rock/paper/scissors)
        # computer_item – the computer’s chosen (random) item (rock/paper/scissors)
        # Return either win, draw, or loss. 
        if user_item == computer_item:
            return 'draw'
        elif (user_item == 'r' and computer_item == 's') or \
             (user_item == 's' and computer_item == 'p') or \
             (user_item == 'p' and computer_item == 'r'):
            return 'win'
        else:
            return 'loss'
            

    def play(self):    
# Get the user’s item (rock/paper/scissors) and remember it
# Get a random item for the computer (rock/paper/scissors) and remember it

        user_item = self.get_user_item()
        computer_item = self.get_computer_item()


# Determine the results of the game by comparing the user’s item and the computer’s item
        result_game =  self.get_game_result(user_item, computer_item)
        
# Print the output of the game; something like this: “You selected rock. 
# The computer selected paper. You lose”, “You selected scissors. The computer selected scissors. You drew!”
        print(f'You selected {user_item}. The computer selected {computer_item}. You {result_game}! ')
        return result_game
    

if __name__ == "__main__":
    game = Game()
    game.play()