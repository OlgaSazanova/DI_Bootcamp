import random
import string
import datetime

#1
class Currency:
    def __init__(self, currency: str, amount : int):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        if self.amount > 1:
            return f"{self.amount} {self.currency}s"
        else:
            return f"{self.amount} {self.currency}"

    def __repr__(self):
        return f"{self.amount} {self.currency}"

    def __int__(self):
        return int(self.amount)

    def __add__(self, other):
        if type(other) == type(self):
            if self.currency == other.currency:
                return Currency(self.currency, self.amount + other.amount)
            else:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
        elif type(other) ==int:
            return Currency(self.currency, self.amount + other)
        else:
            raise TypeError("Operand must be an instance of Currency or an integer")

    def __iadd__(self, other):
        if type(other) == type(self):
            if self.currency == other.currency:
                self.amount += other.amount
                return self
            else:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
        elif  type(other) ==int:
            self.amount += other
            return self
        else:
            raise TypeError("Operand must be an instance of Currency or an integer")


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))  # '5 dollars'
print(int(c1))  # 5
print(repr(c1)) # '5 dollar'

print(c1 + 5)   # '10 dollars'
print(c1 + c2)  # '15 dollars'

print(c1)       # '5 dollars'

c1 += 5
print(c1)       # '10 dollars'

c1 += c2
print(c1)       # '20 dollars'

try:
    print(c1 + c3)  # Raises TypeError
except TypeError as e:
    print(e)        # 'Cannot add between Currency type <dollar> and <shekel>'


#3 Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module


def generate_random_string(length=5):
    letters = string.ascii_letters 
    return ''.join(random.choice(letters) for _ in range(length))

random_string = generate_random_string()
print(random_string)

#4 Create a function that displays the current date.
# Hint : Use the datetime module.

def date_today():
    today_date = datetime.date.today()
    print(today_date)

date_today()

#5 Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).

def left_until_new_year():
    today = datetime.date.today()
    timenow = datetime.datetime.now()
    new_year = "2025-01-01 00:00:00"
    current_time = str(today) + " " + str(timenow.strftime("%H:%M:%S"))
    start = datetime.datetime.strptime(current_time,'%Y-%m-%d %H:%M:%S')
    ends = datetime.datetime.strptime(new_year, '%Y-%m-%d %H:%M:%S')

    print(abs(start - ends))

left_until_new_year()

#6 Create a function that accepts a birthdate as an argument (in the format of your choice), 
# then displays a message stating how many minutes the user lived in his life.

def minutes_lived(birthdate):
    
    bd = datetime.strptime(birthdate, "%Y-%m -%d")
    today = datetime.today()
    min_diff = (today -  bd)/60
    #print(bd)
    #print(today)


    print(f"You lived {min_dif} minutes")

birthdate = input('What is your birthdate? Year-month-day ')
minutes_lived(birthdate)

#7
# Install the faker module, and take a look at the documentation 
# and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. 
# Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.








