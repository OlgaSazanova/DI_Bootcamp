# 1
# Using this code:

class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# Create another cat breed named Siamese which inherits from the Cat class.

class Siamese(Cat):
    def sing(self, sounds):
        return f'{sounds}'
   

# Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
bengal_cat = Bengal('Bengal', 4)
chartreux_cat = Chartreux('Chartreux', 2)
siamese_cat = Siamese('Siamese', 1)
all_cats = [bengal_cat, chartreux_cat, siamese_cat]

# Those three cats are Sara’s pets. Create a variable called sara_pets
#  which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
sara_pets = Pets(all_cats)

# Take all the cats for a walk, use the walk method.
sara_pets.walk()

#2
# Create a class called Dog with the following attributes name, age, weight.
class Dog():
    
    def __init__(self, name : str, age : int, weight: float) -> None:
        self.name = name
        self.age = age
        self.weight = weight

# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.

    def bark(self):
        return f'{self.name} is barking'
 
# run_speed: returns the dogs running speed (weight/age*10).   
    def run_speed(self):
        return self.weight/self.age*10

# fight : takes a parameter which value is another Dog instance, called other_dog.
#  This method returns a string stating which dog won the fight.
#  The winner should be the dog with the higher run_speed x weight.
    def fight(self, other_dog):
        first_dog_fight = self.run_speed() * self.weight
        other_dog_fight = other_dog.run_speed() * other_dog.weight

        if first_dog_fight > other_dog_fight:
            return f'{self.name} wins in fight with {other_dog.name}'
        elif first_dog_fight < other_dog_fight:
            return f'{other_dog.name} wins in fight with {self.name}'
        elif first_dog_fight == other_dog_fight:
            return f'There is no winner'
        
# Create 3 dogs and run them through your class.
dog1 = Dog('Boby', 6, 15.6)
dog2 = Dog('Laly', 2, 4 )
dog3 = Dog('Zuzi', 10, 8.5 )

print(dog1.bark())
print(dog2.bark())
print(dog3.bark())

print(f'{dog1.name} run speed: {dog1.run_speed()}')
print(f'{dog2.name} run speed: {dog2.run_speed()}')
print(f'{dog3.name} run speed: {dog3.run_speed()}')

print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog3.fight(dog1))


#4
# Create a class called Family and implement the following attributes:

# members: list of dictionaries
# last_name : (string)

class Family():
    def __init__(self, last_name : str, members: list) ->  None:
        self.last_name = last_name
        self.members = members
    
# Implement the following methods:
# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f'Congratulations!!! {kwargs['name']} was born!!!')
           
    

# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
        
    def is_18(self, name: str) -> bool:
        for member in self.members:
            if member['name'] == name:
                return member['age'] > 18
        return False

# family_presentation: a method that prints the family’s last name and all the members’ details.    
    def family_presentation(self):
        print(f"The {self.last_name} family members:")
        for member in self.members:
            print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Is Child: {member['is_child']}")

# Create an instance of the Family class, with the last name of your choice, and the below members. 
# Then call all the methods you created in Point 2.

family = Family("Cohen", [
    {'name':'Michael','age':35,'gender':'Male','is_child':False},
    {'name':'Sarah','age':32,'gender':'Female','is_child':False}
])
Bob = {name:'Bob', age:0, gender:'Male', is_child:True}
family.family_presentation()

print(family.is_18('Michael'))  
print(family.is_18('John'))  

family.born(name=Bob['name'], age=Bob['age'], gender=Bob['gender'], is_child=Bob['is_child'])
family.family_presentation()

# 5
# Create a class called TheIncredibles. This class should inherit from the Family class:
# This is no random family they are an incredible family, therefore the members attributes, 
# will be a list of dictionaries containing the additional keys : power and incredible_name. (See Point 4)
# Define the Family class



class TheIncredibles(Family):
    def __init__(self, last_name: str, members: list, power : str, incredible_name : str ):
        super().__init__(last_name, members)

# Add a method called use_power, this method should print the power of a member only if they are over 18 years old.
#  If not raise an exception (look up exceptions) which stated they are not over 18 years old.      

    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] > 18:
                    print(f"{member['name']}'s power: {member['power']}")
                else:
                    raise Exception(f"{member['name']} is not over 18 years old.")

# Add a method called incredible_presentation which :

# Print a sentence like “*Here is our powerful family **”
# Prints the family’s last name and all the members’ details (ie. use the super() function, 
# to call the family_presentation method)

    def incredible_presentation(self):
        print("Here is our powerful family, The Incredibles!")
        super().family_presentation()

# Create an instance of the Incredibles class, with the “Incredibles” last name, and the below members.

new_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
]

incredible_family = TheIncredibles('Incredibles', new_members)

# Call the incredible_presentation method
incredible_family.incredible_presentation

# Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.
incredible_family.born(name='Jack', age=0, gender='Male', is_child=True, power='Unknown Power', incredible_name='Baby Jack')

# Call the incredible_presentation method again
incredible_family.incredible_presentation()







