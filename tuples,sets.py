# tuples immutable      # objects whose value is unchangeable
# list mutable    # objects whose values can change are called mutable

# Some objects contain references to other objects, these objects are called containers. Some examples of containers
# are a tuple, list, and dictionary. The value of an immutable container that contains a reference to a mutable
# object can be changed


# Some of the mutable data types in Python are list, dictionary, set and user-defined classes.

# On the other hand, some of the immutable data types are int, float, decimal, bool, string, tuple, and range.

list_1 = ['math', 'bio', 'physics']
list_2 = list_1

print(list_2)
print(list_1)

list_2[0] = 'kannada'

print(list_2)
print(list_1)

# ['kannada', 'bio', 'physics']
# ['kannada', 'bio', 'physics']


# both the objects get changed

# tuples

tuple_1 = ('math', 'bio', 'physics')
tuple_2 = tuple_1

print(tuple_2)
print(tuple_1)

# stuple_2[0]='kannada'

# TypeError: 'tuple' object does not support item assignment
# if we know the list isn't gonna change , you can use tuple

# Python list method list() takes sequence types and converts them to lists.
# This is used to convert a given tuple into list.
aTuple = (123, 'xyz', 'zara', 'abc')
aList = list(aTuple)

print(aList)
aList.append(345)
print(aList)

aList[0]=456

# SETS ARE UNORDERED , NON DUPLICATE LIST OF ITEMS
# PRINTS IN DIFFERENT ORDER EVERYTIME ITS EXECUTED
# USUALLY USED TO CHECK A VALUE IS PRESENT OR NOT( membership   test)
# and to remove duplicates
# IN APPLICATIONS WHICH ARE NOT PARTICULAR ABOUT ORDER


set_1 = {'math', 'bio', 'physics', 'bio', 'math'}
set_2 = {'math', 'design', 'physics'}
print(set_1)  # {'math', 'bio', 'physics'}

print('bio' in set_1)
# True


# whats common with 2 sets, whats different in 2 sets, whats the union of 2 sets

print(set_1.intersection(set_2))
#   {'physics', 'math'}

print(set_1.difference(set_2))

# {'bio'}

print(set_1.union(set_2))

# {'design', 'bio', 'math', 'physics'}


# little gotcha when creating Empty sets

empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()

my_set={}
print(type(my_set))
# <class 'dict'>
