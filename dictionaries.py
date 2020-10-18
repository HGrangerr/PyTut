#  a dictionary  (also known as  hashmap / accessory arrays in other languages )
# dictionary has unique identifier called key , which has a value called value


# Creating a dictionary
books = {'title': 'War & peace', 'author': 'leo tolstoy', 'isbn': 'uhwhhjhsjshsd', 'price': 345}
books = {
    'title': 'War & peace',
    'author': 'leo tolstoy',
    'isbn': 'uhwhhjhsjshsd',
    'price': 345
}
print(books)
print( 'leo tolstoy' in books)  #False

print(books['title'])
# print(books[saled_copies])
# if we try to access key not defined NameError: name 'saled_copies' is not defined in the dictionary

# so if we want to print none if the key doesnt exist

print(books.get('saled_copies'))  # none
print(books.get('saled_copies', 'unknown'))  # unknown

# add value
books['saled_copies'] = '5 Million'

# change values
books['isbn'] = 'RGFSH09279'

print(books)
# Output: {'title': 'War & peace', 'author': 'leo tolstoy', 'isbn': 'RGFSH09279', 'price': 345, 'saled_copies': '5
# Million'}

# UPDATE MULTIPLE VALUES AT A TIME
books.update({'price': 456, 'author': 'Leo Tolstoy'})
print(books)

# {'title': 'War & peace', 'author': 'Leo Tolstoy', 'isbn': 'RGFSH09279', 'price': 456, 'saled_copies': '5 Million'}

# Delete

del books['isbn']
print(books)

# {'title': 'War & peace', 'author': 'Leo Tolstoy', 'price': 456, 'saled_copies': '5 Million'}

# pop
amt = books.pop('price')
print(amt)
# 456

print(books.values())
# dict_values(['War & peace', 'Leo Tolstoy', '5 Million'])

print(books.keys())
#


print(books.items())
#

for item in books:
    print(item)
print('\n\n')
# this is just gonna print out keys
# title
# author
# saled_copies

for key, value in enumerate(books):
    print(key, value)
print('\n\n')

# only keys again
# 0 title
# 1 author
# 2 saled_copies

for key, value in books.items():
    print(key, value, sep=':')
print('\n\n')

# title:War & peace
# author:Leo Tolstoy
# saled_copies:5 Million
nums =[1,2,3]
my_list = [n for n in nums]
print(my_list)