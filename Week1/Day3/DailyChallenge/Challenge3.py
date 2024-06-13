#1.
#Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.
# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.

user_word=input('Write a word: ')


word_to_dict = {}
for index, letter in enumerate(user_word):
    if letter not in word_to_dict:
        word_to_dict[letter]=[index]
    else:
        word_to_dict[letter].append(index)

print(type(word_to_dict))
print(word_to_dict)


#2
# Create a program that prints a list of the items you can afford in the store
# with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.


items_purchase = {
  "Apple": "$4",
  "Honey": "$3",
  "Fan": "$14",
  "Bananas": "$4",
  "Pan": "$100",
  "Spoon": "$2"
}

print(items_purchase)
items_purchase_new={}

#convert the amount from dollars to numbers:
items_purchase_new={item:price.replace('$', '') for (item, price) in items_purchase.items()}
items_purchase_new={item:price.replace(',', '') for (item, price) in items_purchase_new.items()}
items_purchase_new={item:float(price) for (item, price) in items_purchase_new.items()}

money=input('Write amount of money that you have in your wallet: ')
money = float(money)

# make a list of affordable items
items_to_buy = []

for item, price in items_purchase_new.items():
    if price <= money:
        items_to_buy.append(item)


# Sort the list in alphabetical order.
items_to_buy=sorted(items_to_buy)

if items_to_buy == []:
    print('Nothing')
else:
    print(f'You can buy: {items_to_buy} ')






