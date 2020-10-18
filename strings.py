name = "hello world"  # double quotes
place = 'mysore'  # single quote

new_name = "Bobby's world"
new_name = 'Bobby\'s world'

# If you must use a " or ' between the same quote escape it with \

string_name = 'python for "beginners" '

# multiline

msgs = '''hi
hello
here'''

print(name, place, new_name, string_name, "\n", msgs)
# output:hello world mysore Bobby's world python for "beginners"
# hi
# hello
# here


# To embed a string in output use %s
print("{} ,{} ! {} {} {}".format('I like the quote', ":", string_name, ":", msgs))
print("%s %s %s %s %s" % ('I like the quote', ":", string_name, ":", msgs))

# I like the quote python for "beginners"  hi
# hello
# here

# To keep from printing newlines use end=""
print("I don't like ", end="")
print("newlines")

# I don't like newlines

# You can print a string multiple times with *
print('\n' * 5)

name.upper()  # wont work if not assigned back to string,not inplace,immutable
print(name)  # Output:hello world
print(name.upper())  # HELLO WORLD
name = name.upper()  # works
print(name)

# HELLO WORLD


# single line comment

# multiline '''Python will ignore string literals that are not assigned to a variable, you can add a multiline string
# (triple quotes) in your code, and place your comment inside it:'''
# As long as the string is not assigned to a variable, Python will read the code, but then ignore it, and you have
# made a multiline comment

multiline = "Python will ignore string literals that are not assigned to a variable," \
            "you can add a multiline string" \
            "(triple quotes) in your code, and place your comment inside it:"

print(multiline)

# \ is called continuity character , prints the above line in single line


print(name[0])  # H
print(name[-1])  # D
print(name[-2])  # L

print(name[0:5])  # HELLO
print(name[:5])  # HELLO
print(name[6:])  # WORLD

# string slicing


no_of_o = name.count('o')  # 0
no_of_o = name.lower().count('o')  # 2
index_of_s = place.find('s')  # 2
print(no_of_o, index_of_s)

new_msg = name.replace('WORLD', 'UNIVERSE')
print(new_msg)
# HELLO UNIVERSE


concat_str = name + " ," + new_msg
print(concat_str)
# HELLO WORLD ,HELLO UNIVERSE

# string formatting
msg = '{},{},Welcome!'.format(name, concat_str)
# {} are called placeholders

message = f'{name},{concat_str.capitalize()},Welcome!'
print(message)  # HELLO WORLD,Hello world ,hello universe,Welcome!

print(msg)  # HELLO WORLD,HELLO WORLD ,HELLO UNIVERSE,Welcome!

print(len(msg))  # 48
# print(dir(name))
#
# print(help(concat_str.capitalize))
# print(help(str))

# The str(), int(), and float() Functions
# If you want to concatenate an integer such as 29 with a string to pass to
# print(), you’ll need to get the value '29', which is the string form of 29. The
# str() function can be passed an integer value and will evaluate to a string
# value version of it, as follows:
# >>> str(29)
# '29'


# num = print(str(29) + '2')  # 292
print(str(29) + '2') # 292
# print(num)  # none print returns nothing
