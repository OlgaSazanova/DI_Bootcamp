# Given this list:


# list1 = [5, 10, 15, 20, 25, 50, 20]


# find the value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value


# Hint : Look at the index method

list1 = [5, 10, 15, 20, 25, 50, 20]
for i in list1:
    if i ==20:
        i*=10
        break
print(list1)



a_tuple = (10, 20, 30, 40)
a, b, c, d = a_tuple
print(a)
print(b)
print(c)
print(d)