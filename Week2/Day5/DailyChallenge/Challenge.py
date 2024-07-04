# 1. Answer the following questions

# What is a class?
#Classes are used to create new user-defined data structures that contain arbitrary information about something. 
# A class provides structure—it’s a blueprint for how something should be defined, 
# but it doesn’t offer any actual content itself.

# What is an instance?
# An instance is a copy of the class with actual values, literally an object belonging to a specific class. 

# What is encapsulation?
# Encapsulation is the binding of data and functions that manipulate that data and
# we encapsulate into one big object so that we keep everything in this box that users or code or other
# machines can interact with in this data

# What is abstraction?
#Abstraction means hiding of information or abstracting away information
#and giving access to only what’s necessary.

# What is inheritance?
# Inheritance is the process by which one class takes on the attributes and methods of another.
# Newly formed classes are called child classes,
# and the classes that child classes are derived from are called parent classes.

# What is multiple inheritance?
# A class can inherit from two different classes; in this case, 
# the order of the parent class in a class definition will decide what will be inherited.
# The first parent class will prioritize classes below (meaning the functions last to be inherited 
# can override functions from the parent class).

# What is polymorphism?
# In programming, polymorphism means different or related classes that use the same names for their functions.
#Polymorphism allows the ability to use a standard interface for multiple forms or data types.

# What is method resolution order or MRO?
#Method Resolution Order (MRO) in Python is the order in which base classes are searched when executing a method.
#  This is especially important in multiple inheritance scenarios.


#2
# The Deck of cards class should NOT inherit from a Card class.

# The requirements are as follows:

import random
# The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
class Card:
    def __init__(self, suit, value) -> None:
        self.suit = suit
        self.value = value

    def define_cards(self, suit, value):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{self.value} of {self.suit}'


# The Deck class :
# should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
# should have a method called deal which deals a single card from the deck.
class Deck:
    def __init__(self) -> None:
        suits = Card.suits
        values = Card.values
        self.cards = [Card(suit, value) for suit in suits for value in values]

   
    def shuffle(self):
        if len(self.cards) != 52:
            self.cards = [Card(suit, value) for suit in self.suits for value in self.values]
            random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            return "No cards left to deal"
        return self.cards.pop()

#  After a card is dealt, it should be removed from the deck.



deck = Deck()
print("Initial shuffled deck:")
print(deck.cards)

dealt_card = deck.deal()
print("Dealt card:")
print(dealt_card)

print("Deck after dealing one card:")
print(deck.cards)