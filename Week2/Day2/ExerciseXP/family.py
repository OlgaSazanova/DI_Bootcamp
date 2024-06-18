class Family:
  def __init__(self, last_name: str, members: list) -> None:
    self.last_name = last_name
    self.members = members

  def born(self, **kwargs):
    self.members.append(kwargs)
    print(f'Congratulations!!! {kwargs["name"]} was born!!!')

  def is_18(self, name: str) -> bool:
    for member in self.members:
      if member['name'] == name:
        return member['age'] > 18
    return None

  def family_presentation(self):
    print(f"The {self.last_name} family members:")
    for member in self.members:
      print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, Is Child: {member['is_child']}")

# Create an instance of the Family class
family = Family("Cohen", [
  {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
  {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
])

family.family_presentation()  # Print initial family details

# Unpack the Bob dictionary using **kwargs
family.born(name=Bob['name'], age=Bob['age'], gender=Bob['gender'], is_child=Bob['is_child'])

print(family.is_18('Michael'))
print(family.is_18('John'))
family.family_presentation()  # Print updated family details
