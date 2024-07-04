#1
# Using this class

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
# Instantiate three Cat objects using the code provided above.

# v.1
def get_oldest_cat(cat_list: list[Cat]) -> Cat:
    oldest_cat = cat_list[0]

    for cat in cat_list:
         if cat.age > oldest_cat.age:
             
             oldest_cat = cat
    return oldest_cat

#v.2
def get_cat_age(cat:Cat) -> int:
    return cat.age

def main():
    first_cat = Cat('Mini', 3 )
    second_cat = Cat('Hatul', 1)
    third_cat = Cat('Shon', 5)

    cats = [first_cat, second_cat, third_cat]

    # oldest_cat = get_oldest_cat(cats)

    oldest_cat = max(cats, key = get_cat_age )

    print(f'The oldest cat is {oldest_cat.name}, and is {oldest_cat.age} years old.')


if __name__ == "__main__": # Run the code below if you run the file directly
    main()


#2
# Create a class called Dog.
# In this class, create an __init__ method that takes two parameters : name and height.
# This function instantiates two attributes, which values are the parameters.


class Dog:
    def __init__(self, name : str, height : float) -> None:
        self.name = name
        self.height = height
# Create a method called bark that prints the following string “<dog_name> goes woof!”.

    def bark(self) -> None:
        print(f'{self.name} goes woof!')

# Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
    def jump(self) -> None:
        jump_height = self.height *2
        print(f'{self.name} jumps {jump_height} cm high!')

# This function presents a dog - give info about name and height
    def present_dog(self) -> None:
        print(f"Dog name: {self.name}. Height: {self.height}")



    
# Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# Print the details of his dog (ie. name and height) and call the methods bark and jump.
# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump.
# Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.


def get_dog_height(dog:Dog) -> float:
    return dog.height

def main():
    david_dog = Dog(name='Rex', height=50)

    david_dog.present_dog()
    david_dog.bark()
    david_dog.jump()
    

    sarahs_dog = Dog('Teacup', 20)
    sarahs_dog.present_dog()
    sarahs_dog.bark()
    sarahs_dog.jump()
   

    dogs = [david_dog, sarahs_dog]


    biggest_dog = max(dogs, key = get_dog_height )   
    
    print(f"{biggest_dog.name} is the biggest dog in town!")
    

if __name__ == "__main__": # Run the code below if you run the file directly
    main()


#3
# Define a class called Song, it will show the lyrics of a song.
# Its __init__() method should have two arguments: self and lyrics (a list).

class Song:
    def  __init__(self, lyrics : list) -> None:
        self.lyrics = lyrics
# Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
    def sing_me_a_song(self) -> None:
        for line in self.lyrics:
            print(line)
   


def main():
    stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
    stairway.sing_me_a_song()



if __name__ == "__main__": # Run the code below if you run the file directly
    main()

#4
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).

class Zoo:
    def __init__(self, zoo_name: str):
        self.name = zoo_name
        self.animals = []


# Create a method called add_animal that takes one parameter new_animal.
# This method adds the new_animal to the animals list as long as it isn’t already in the list.
    def add_animal(self):
        new_animal = input('Which animal should we add to the zoo? ')
        if new_animal not in self.animals:
            self.animals.append(new_animal)
            print(f"{new_animal} added to the zoo!")
        else:
            print(f"{new_animal} is already in the zoo.")
    

# Create a method called get_animals that prints all the animals of the zoo.
    def get_animals(self):
        if self.animals:
            print(f"Animals in {self.name}:")
            for animal in self.animals:
                print(animal)
        else:
            print("No animals in the zoo.")

# Create a method called sell_animal that takes one parameter animal_sold.
#  This method removes the animal from the list and of course the animal needs to exist in the list.
    def sell_animal(self):
        animal_sold = input('Which animal should we sell? ')
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
            print(f"{animal_sold} has been sold.")
        else:
            print(f"{animal_sold} is not in the zoo.")

# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Example

# { 
#     1: "Ape",
#     2: ["Baboon", "Bear"],
#     3: ['Cat', 'Cougar'],
#     4: ['Eel', 'Emu']
# }

    # def sort_animals(self):
    #     animal_groups = {}
    #     sorted_animals = sorted(self.animals, key=str.upper)
    #     group_number = 1

    #     for animal in sorted_animals:
    #         if group_number not in animal_groups:
    #             animal_groups[group_number] = [animal]
    #         else:
    #             animal_groups[group_number].append(animal)
    #         group_number += 1

    #     return animal_groups
    

    def sort_animals(self):
        animal_groups = {}
        sorted_animals = sorted(self.animals)
        for animal in sorted_animals:
            first_letter = animal[0].upper()
            if first_letter not in animal_groups:
                animal_groups[first_letter] = [animal]
            else:
                animal_groups[first_letter].append(animal)
        
        grouped_animals = {}
        group_number = 1
        for key in sorted(animal_groups.keys()):
            grouped_animals[group_number] = animal_groups[key] if len(animal_groups[key]) > 1 else animal_groups[key][0]
            group_number += 1
        
        return grouped_animals
# Create a method called get_groups that prints the animal/animals inside each group.
    def get_groups(self):
        animal_groups = self.sort_animals()
        for key in sorted(animal_groups.keys()):
            print(f"{key}: {animal_groups[key]}")


#Create an object called ramat_gan_safari and call all the methods
def main():
    ramat_gan_safari = Zoo('Ramat Gan Safari')

    ramat_gan_safari.add_animal()
    ramat_gan_safari.get_animals()
    ramat_gan_safari.sell_animal()
    ramat_gan_safari.get_animals()
    ramat_gan_safari.get_groups()

if __name__ == "__main__": # Run the code below if you run the file directly
    main()