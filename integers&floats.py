# type

number = 3
float_no = 3.14
print(type(number), type(float_no))

# Arithmetic operators

add = float(number) + float_no
print('Sum of {0} and {1} is {2}'.format(float(number), float_no, add))
# Sum of 3.0 and 3.14 is 6.14

subs = float_no - number

division = 10 / 4
floor_div = 10 // 4

mul = 10 * 4.5

expo = 10 ** 3

mod = 10 % 2

print(number, add, subs, division, floor_div, mul, expo, mod)
# precedence , pemdas rule
# Order of operation use parenthesis

x1 = 5
y1 = 5
print(x1 is not y1)  # False
print(id(x1) != id(y1))  # False
print(id(x1), id(y1))

# primitive var stores the value of the var , whereas obj ref var refers to id (place in mm)
# 1609934832 1609934832


# Increments 2 ways

number = number + 1
print('num', number)
number += 1
print('num', number)

print('num', number)

# abs(negative) =positive

nega_no = -4

print('nega', abs(nega_no))

# round(num) rounds to nearest int

print(round(3.55))

# round(num,1) round to first digit after decimal
print(round(3.55, 1))

# Comparisons

print(23 == 43)

print(23 != 34)

print(23 < 34)

print(23 > 34)
print(23 >= 34)

print(23 <= 34)

# Type casting
string_num = '24'
print(int(string_num) + 2)  # 26

a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
print(a)

# \ continuation character
width = 17
print(width // 2)  # 8
print(width / 2.0)  # 8.5
print(1 + 2 * 5)  # 11
print(5 + 30 - 4 * 20 / 12 // 3 % 2 ** 2)

print(15 / 3 * 2.5 % 2 ** 2)
#
print(5 * 3 / 2.5 % 2 ** 2)

print(4)

from random import *
print(randint(2,5))

