

#1
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dict1=dict(zip(keys, values))

print(dict1)

#2
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Given the following object:

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# How much does each family member have to pay ?
family_total = 0
for key, value in family.items():
    if value <= 3:
        print(f'{key}, your ticket price: $0')
        
    if 3 < value < 12:
        print(f'{key}, your ticket price: $10')
        family_total +=10
    if value > 12:
        print(f'{key}, your ticket price: $15')
        family_total +=15

# Print out the family’s total cost for the movies.

print(family_total)

# Bonus: Ask the user to input the names and ages instead of using the provided family variable
# (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).

family_2={}


names=input('Please, provide the names of your family, separate using comma: ')
names = names.split(', ')
ages = input('Please, provide the ages of your family, separate using comma: ')
ages = ages.split(', ')
ages = [int(i) for i in ages]  # convert strings to integers
family_2 = dict(zip(names, ages)) # creat a dictionary

print(family_2)

#3
    #Create a dictionary called brand which value is the information from part one
    #  (turn the info into keys and values).
    #The values type_of_clothes and international_competitors should be a list. 
   # The value of major_color should be a dictionary.
brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'], 
    'international_competitors': ['Gap', 'H&M', 'Benetton'], 
    'number_stores': 7000,
    'major_color': {
        'France': 'blue', 
        'Spain': 'red', 
        'US': ['pink', 'green']}
    }

#Change the number of stores to 2.

brand['number_stores']= 2
print(brand)

# Print a sentence that explains who Zaras clients are.


print('Zaras clients are ' + brand['type_of_clothes'][0]+ ', ' + brand['type_of_clothes'][1] +' and ' + brand['type_of_clothes'][2] + '.')

#  Add a key called country_creation with a value of Spain.
brand['country_creation'] = 'Spain'
# Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.

print('international_competitors' in brand) # True
brand['international_competitors'].append('Desigual')
print(brand['international_competitors'])

# Delete the information about the date of creation.
del brand['creation_date']
print(brand)

#Print the last international competitor
print(brand['international_competitors'][-1])

# Print the major clothes colors in the US.

print(brand['major_color']['US'])

# Print the amount of key value pairs (ie. length of the dictionary).
print(brand)
print(len(brand))

#Print the keys of the dictionary.
print(brand.keys())

#  Create another dictionary called more_on_zara with the following details:

# creation_date: 1975 
# number_stores: 10 000
more_on_zara ={}
more_on_zara['creation_date'] = 1975
more_on_zara['number_stores'] = 10000

print(more_on_zara)

# Use a method to add the information from the dictionary more_on_zara to the dictionary brand.

brand.update(more_on_zara)
print(brand)

#14. Print the value of the key number_stores. What just happened ?
print(brand['number_stores']) # the value was updated using info from more_on_zara



#4 Use this list :

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
#Analyse these results :

#1/

# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.

disney_users_A ={}
disney_users_A = {user : index for index, user in enumerate(users)}

print(disney_users_A)



#2/

# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
#Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
disney_users_B ={}
disney_users_B = {index : user for index, user in enumerate(users)}
print(disney_users_B)


#3/ 

# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
disney_users_C ={}
users_sort = users
users_sort.sort()
print(users_sort)

disney_users_C ={user :index for index, user in enumerate(users_sort)}
print(disney_users_C)


#Only recreate the 1st result for:
# The characters, which names contain the letter “i”:
# # >>> print(disney_users_A_i)
# {"Mickey": 0, "Minnie": 1,  "Ariel": 3}

disney_users_A_i ={}
disney_users_A_i = {user : index for index, user in enumerate(users) if 'i' in user}
print(disney_users_A_i)


# The characters, which names start with the letter “m” or “p”.
disney_users_A_mp ={}
disney_users_A_mp = {user : index for index, user in enumerate(users) if  (user[0]== 'M' or user[0] == 'P')}
print(disney_users_A_mp)