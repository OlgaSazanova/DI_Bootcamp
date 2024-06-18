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