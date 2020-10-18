# List
from itertools import chain

names = ['rach', 'aara', 'akka', 'amma']
print(names)
names[3] = "srggghg"  # replaces the value , but cant be used to extend the list
print(names)

names = ['rach', 'aara', 'akka', 'amma']
print(names[0])
print(len(names))
print(
    names[-1])  # as the list grows , length night change so last index no might change , but -1 will always be the last
print(names[-2])

# slicing
print(names[0:])
# also
print(names[:])

print(names[:-2])
print(names[0:2])
print(names[:2])
print(names[3:])

print(names[-1:])
print(names[:-1:2])  # step 2

# modifying lists
# many ways  1)append() 2)insert(pos, value) 3)extend() 4) + operator  5) slicing 6) Using chain()

names.append('appa')  # add at end of list

names.insert(0, 'atharv')  # insert at required position

# names.insert(1, 5)
# Traceback (most recent call last):
#   File "C:/Users/User/Desktop/py tutorial/List,tuples,sets.py", line 90, in <module>
#     names.sort()
# TypeError: '<' not supported between instances of 'int' and 'str'


some_more = ['tush ', 'tarun']

# names.insert(-1, some_more)

# becomes ['atharv', 'rach', 'aara', 'akka', 'amma', ['tush ', 'tarun'], 'appa']

# but we want to have the individual entries on the list, use extnd function

names.extend(some_more)

# becomes ['atharv', 'rach', 'aara', 'akka', 'amma', 'appa', 'tush ', 'tarun']
# this is not to be confused with the append , what append does is this
# ['atharv', 'rach', 'aara', 'akka', 'amma', ['tush ', 'appa','tarun']]


# Using ‘+’ operator:

names = names + some_more + ['hi', 'hello']

print(names)
# ['atharv', 'rach', 'aara', 'akka', 'amma', 'appa', 'tush ', 'tarun', 'tush ', 'tarun', 'hi', 'hello']

# Python program to extend a list using 'slicing'

# appending multiple value
a = [10, 12, 13, 17]

# add 1 number
a[:0] = [30]

# add two numbers
a[:0] = [40, 50]

a[1:3] = [50, 60]
print(a)  # [40, 50, 60, 10, 12, 13, 17]

# a[-1:] = [90,29] this omits 17
a.extend([90, 29])
print(a)
# [40, 50, 30, 10, 12, 13, 17, 90, 29]
# in slicing values are added at start
# Using chain():  list(chain(a, [x, y, z..]))

# python program to extend a list using
# "chain" iterator functions


a = [10, 20, 30]

# extend a list
print(list(chain(a, [40, 50, 60])))
# Output:[10, 20, 30, 40, 50, 60]

# remove
names.remove('tarun')
print(names)
# pop


names.pop()
print(names)

# reverse        1) reverse   2) slicing 3) sort(reverse=True
names.reverse()
print(names)

# names = ['rach', 'aara', 'akka', 'amma']
print(names[::-1])
# ['amma', 'akka', 'aara', 'rach']

# sort
names.sort()
print(names)

names.sort(reverse=True)
print(names)

a.sort()
print(a)
# print(a.sort()) wont work ,
# coz sorting takes place in place and it returns none , so none is displayed if we call it inside of print statement


revised_names = sorted(names)
print(revised_names)

minimum = min(a)
maximum = max(a)
sum_of = sum(a)

idx = names.index('atharv')

# Python’s membership operators (in) test for membership in a sequence,
# such as strings, lists, or tuples. There are two membership operators as explained below −

print(idx, 'tush' in names)
print('tush' in revised_names)

print('\n')

for index in names:
    print(index)
print('\n')

for index, name in enumerate(names):
    print(index, name)

print('\n')

for index, name in enumerate(names, start=1):
    print(index, name)
print('\n')
fam = '(^)'.join(names)

print(fam)

new_names = fam.split('(^)')

print(new_names)

del names
# print(names)

li = [1, 3, 5, 7, 8]
li.clear()
print(li)

li1 = [1, 3, 5, 7, 8]
li2 = li1.copy()
print(li2)

names = [1, 'aara', 'akka', 'amma']

li = [1, 3, 5, 7, 8, 8, 8]
print(li.count(8))  # 3 count the no of occurrences of a particular element
