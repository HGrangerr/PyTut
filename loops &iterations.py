# loops  and iterations

nums = [1,2,3,45,5]

for index in nums:
    print(index)

# 1
# 2
# 3
# 45
# 5
print('\n')
for index in nums:
    if index == 3:
        print('found')
        break
    print(index)

print('\n')
# break statement breaks out of the loop
# 1
# 2
# found

for index in nums:
    if index == 3:
        print('found')
        continue
    print(index)

# #1
# 2
# found
# 45
# 5
# continue moves to next iteratio

for index in nums:
    if index == 3:
        print('found')
    print(index)

# #1
# 2
# found
# 3
# 45
# 5

# nested for loops

for index in nums:
    for letter in'abc':
        print(index,letter)
    print('\n')

for i in range(5):
    print(i)
print('\n')
# 0
# 1
# 2
# 3
# 4

for i in range(1,5):
    print(i)
print('\n')
#
# 1
# 2
# 3
# 4

x = 0
while x < 10:
    print(x)
    x += 1
print('\n')

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

x = 0
while x < 10:
    if x==5:
        break
    print(x)
    x += 2
print('\n')

# 2
# 4
# 6
# 8

# infinite loop
# while True:
#     print(x)
#     x += 2
