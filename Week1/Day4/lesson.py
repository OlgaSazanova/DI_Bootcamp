# def say_hello():
#     print('Hello there!')

# say_hello()

# def say_hello(name):
#     print(f'Hello {name}')

# say_hello('Olga')

# More that one argument

def say_hello(username: str, language = 'EN'):
    '''prints a greeting depending on user's language'''
    if language == 'EN':
        print(f'Hello, {username}')   
    elif language == 'HE':
        print(f'Shalom, {username}')   
    elif language == 'FR':
        print(f'Bonjour, {username}')   
    elif language == 'PT':
        print(f'Oi, {username}')  
    else:
        print(f'Sorry, there is no languge {language}') 

say_hello('JUliana', 'PT') #positional argument
say_hello(username='Olga', language = 'HE') #keyword arguments
    

# default values - =put for example language ='FR'
say_hello('Ben', 'FR')

# def user_info(username= 'none', email = 'gmail', age = 18, password = None):
#     print('user info ', username, email, age, password)

# user_info('Olga', age = 36)

#global - use somthing not from function, but global
count = 1
def calculation(a,  b):
    global count
    result = a+b
    count+=1
    return result
calculation(4, 6)
print(count)

def sum_total():
    calc1 = calculation(5, 3)
    calc2 = calculation(10, 4)

    result = calc1 + calc2

    return result

print(sum_total())


students= ['Harry', 'Rom', 'Ben', 'Luba']
students_2= ['Maria', 'Kor', 'hen']
def wizard(student_list):
    for name in student_list:
        print(f'{name}, you are a wizard')

wizard(students_2)

def student_house():
    for i,  name in enumerate(students):
        students[i] =f' {name} - house: Gryffindor'

student_house()
print(students)
    

#*args

def emails_list(*usernames):
    emails_list = []
    for user in usernames:
        user_email = user+ '@gmail.com'
        emails_list.append(user_email)

    return emails_list

print(emails_list('sgsgh', 'sghhb', 'sfewvc'))

#**kwargs

def user_info(**kwargs):
    return kwargs

print(user_info(name = 'OLga', email = 'ngsioghswi', age = 36))


#map()

def uppers_list(string):
    return string.upper

fruit = ['D', 'fdfs', 'sgs']

map_obj = map(uppers_list, fruit)
print(list(map_obj))

#filter
def starts_with(string):
    return string[0] == 'A'

fruit2 = ["Apple", "Banana", "Pear", "Apricot", "Orange"]

filtered= list(filter(starts_with, fruit2))
print(filtered)

#reduce

def sum_numbers(a, b):
    return a+b
my_list = [1, 3, 5, 6]
reduced_list = reduce(sum_numbers, my_list)
print(reduced_list)

#lambda

lambda s: s.upper()

map_obj = map(lambda s: s.upper(), fruit)

print(list(map_obj))


people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]

def short_name(name):
    if len(name)<= 4:
        print(f'Hello {name}')

map_obj3=map(short_name, people)
print(list(map_obj3))


people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]


def short_name2(name):
    if len(name)<=4:
        return name
    
filtered_names= str(filter(short_name2, people))
print(f'Hello {filtered_names}')