# Take a look at the following code and output:
# File: market.py

# macdonald = Farm("McDonald")
# macdonald.add_animal('cow',5)
# macdonald.add_animal('sheep')
# macdonald.add_animal('sheep')
# macdonald.add_animal('goat', 12)
# print(macdonald.get_info())
# 
# Output

# McDonald's farm

# cow : 5
# sheep : 2
# goat : 12

#     E-I-E-I-0!


# Create the code that is needed to receive the result provided above.
#  Below are a few questions to assist you with your code:

# Create a class called Farm. How should it be implemented?
# Does the Farm class need an __init__ method? If so, what parameters should it take?
# How many methods does the Farm class need?  - Three

class Farm:
    def __init__(self, name: str) -> None:
        self.name = name
        self.animals = {}

       
    def add_animal(self, animal : str, quantity : int = 1) -> None:
        if animal  in self.animals:
            self.animals[animal] += quantity
        else:
            self.animals[animal] = quantity

# Do you notice anything interesting about the way we are calling the add_animal method?
#  What parameters should this function have? How many…? 

# Yes,  it can be write the quantity of animals, or can be only the name of animal. It means that quantity = 1

    def get_info(self) -> str:
        info = f"{self.name}'s farm\n\n"
        for animal, quantity in self.animals.items():
            info += f"{animal} : {quantity}\n"
        info += "\n    E-I-E-I-O!"
        return info
    
# Add a method called get_animal_types to the Farm class.
#  This method should return a sorted list of all the animal types (names) in the farm.  
    def get_animal_types(self ) -> list:
        animal_types = []
        animal_types = sorted(self.animals.keys())
        return animal_types
    
# Add another method to the Farm class called get_short_info.
#  This method should return the following string: “McDonald’s farm has cows, goats and sheeps.”. 
#  The method should call the get_animal_types function to get a list of the animals. 

    def get_short_info(self) -> str:
        animal_types = self.get_animal_types()
        animal_types_str = ", ".join(f"{animal_type}s" for animal_type in animal_types)
        return f"{self.name}'s farm has {animal_types_str}."



def main():
    macdonald = Farm("McDonald")
    macdonald.add_animal('cow',5)
    macdonald.add_animal('sheep')
    macdonald.add_animal('sheep')
    macdonald.add_animal('goat', 12)
    print(macdonald.get_info())

    print(macdonald.get_short_info())


if __name__ == "__main__": # Run the code below if you run the file directly
    main()






