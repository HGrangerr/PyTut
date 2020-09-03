# type

number = 3
float_no = 3.14
print(type(number), type(float_no))

# Arithmetic operators

add = number + float_no
subs = float_no - number

division = 10 / 4
floor_div = 10 // 4

mul = 10 * 4.5

expo = 10 ** 3

mod = 10 % 2

print(number, add, subs, division, floor_div, mul, expo, mod)

# Order of operation use parenthesis


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
print(int(string_num))
