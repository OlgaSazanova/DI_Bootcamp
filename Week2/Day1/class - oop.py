class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def show_details(self):
    print("Hello my name is " + self.name)

  def change_name(self):
    print('Now your name is Big' +self.name)

first_person = Person("John", 36)
first_person.show_details()
first_person.change_name()

