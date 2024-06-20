import game

# get_user_menu_choice() - this should display a simple menu, 
# get the user’s choice (with data validation), and return the choice. No looping should occur here.
# The possibles choices are : Play a new game or Show scores or Quit

def get_user_menu_choice():
    
    while True:

        first_input = input('Menu: \n(g) Play a new game \n(x) Show scores and exit ')
        first_input = first_input.strip().lower()
        if  first_input in ['g', 'x']:
            return first_input
        else: 
            print('Invalid choice. Please enter "g" or "x".')


# print_results(results) – this should print the results of the games played.
#  It should display these results in a user-friendly way, and thank the user for playing.
# Note: results should be in this form: {win: 2,loss: 4,draw: 3}. 
# Bear in mind that this dictionary will need to be created and populated in some other part of our code,
#  and passed in to the print_results function at the right time.

def print_results(results):
    print('   Game results')
    print(f'You won {results["win"]} times')
    print(f'You lost {results["loss"]} times')
    print(f'You drew {results["draw"]} times')
    print()
    print('Thank you for playing!')


def main():
    game_obj = game.Game()
    results = {'win': 0, 'loss': 0, 'draw': 0}

        
    while True:
        choice = get_user_menu_choice()
        if choice == 'g':
            result = game_obj.play()
            if result == 'win':
                results['win'] += 1
            elif result == 'loss':
                results['loss'] += 1
            elif result == 'draw':
                results['draw'] += 1
        elif choice == 'x':
            print_results(results)
            break

if __name__ == "__main__":
    main()
    


    



