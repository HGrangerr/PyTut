# List
from itertools import chain

names = ['rach', 'aara', 'akka', 'amma']
print(names)

print(names[0])
print(len(names))
print(
    names[-1])  # as the list grows , length night change so last index no might change , but -1 will always be the last
print(names[-2])

# slicing
print(names[0:])
print(names[0:2])
print(names[:2])
print(names[3:])

# modifying lists
# many ways  1)append() 2)insert(pos, value) 3)extend()

names.append('appa')  # add at end of list

names.insert(0, 'atharv')  # insert at required position

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

# Python program to extend a list using 'slicing'

# appending multiple value
a = [10, 12, 13, 17]

# add 1 number
a[:0] = [30]

# add two numbers
a[:0] = [40, 50]
a[-1:] = [90]

print(a)
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
# reverse

names.reverse()
print(names)

# sort
names.sort()
print(names)

names.sort(reverse=True)
print(names)

a.sort()
print(a)
# print(a.sort()) wont work

revised_names = sorted(names)
print(revised_names)

minimum = min(a)
maximum = max(a)
sum_of = sum(a)

idx = names.index('atharv')

print(idx, 'tush' in names)
print('tush' in revised_names)

print('\n')

for index in names:
    print(index)
print('\n')

for index,name in enumerate(names):
    print(index,name)

print('\n')

for index, name in enumerate(names,start=1):
        print(index, name)
print('\n')
fam = '(^)'.join(names)

print(fam)

new_names = fam.split('(^)')

print(new_names)
