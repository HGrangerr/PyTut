# functions
# functions are a set of instructions packaged together for doing specific tasks
# to create a func in py,
# we need to use the keyword def,which maybe stands for definition , and then give the name of the function

def func_one():
    pass


# do nothing func , it doesnt throw an error , use this if we want to skip it for now , provide functionality  later

print(func_one)

# now , if we print the func without paranthesis
# <function func_one at 0x01384190>
# prints out the what it is , func at mem loc ,doesnt execute

print(func_one())


# None
# coz the func does nothing

def func_one():
    print('Hi there hows it goin!')


func_one()
# Hi there hows it goin!

print(func_one())


# None
# coz it returns nothing


# one main benefit of the func is reusability
# ex if we have some text which is repeating itself in our program for n times,
# we can put it in a func and use that n times
# this is helpful in situations where if we want to make any changes to the code ,
# we dont have to change all n lines but instead change in that one function
# so functions allow us to put code which does a specific thing in a func, single location ,
# and use it multiple times, and if we want to change , change it once , inside the func
# , and change is reflected everywhere
# so this is called DRY (Don't Repeat Yourself)


def func_hello():
    return 'hello'


func_hello()

# does nothibg

print(func_hello())
# hello

# so you  can think of a func as some machine which takes in input and produces some output
# or a blackbox , you don't need to know hows its doing what its doing

# we can treat the return value as the data type itself
# ex if a func returns a string, we can apply all methods of string on it
# for ex

print(func_hello().upper())


# HELLO

# passing arguments

def func_hello(msg):
    return '{} !welcome'.format(msg)


# print(func_hello())
# TypeError: func_hello() missing 1 required positional argument: 'msg'

print(func_hello('hi'))


# hi !welcome

def func_hello(msg, name):
    return '{} {} ! ,welcome'.format(msg, name)


print(func_hello('hi', 'rach'))


# hi rach ! ,welcome

#  if we want a default value to be printed when we dont pass in anything

def func_hello1(msg, name='yo'):
    return '{} {} ! ,welcome'.format(msg, name)


print(func_hello1('hi'))

# hi yo ! ,welcome

print(func_hello('hi', name='corey'))
# hi corey ! ,welcome
print(func_hello('hi', 'rach'))
# hi rach ! ,welcome

# Python functions can contain two types of arguments:
# positional arguments and keyword arguments.
# Positional arguments must be included in the correct order.
# Keyword arguments are included with a keyword and equals sign.
#
# Positional Arguments
# Positional arguments are arguments that need to be included in the proper position or order.
# The first positional argument always needs to be listed first when the function is called.
# The second positional argument needs to be listed second

# Keyword Arguments
# A keyword argument is an argument passed to a function or method which is preceded by a keyword and an equals sign.
# The general form is:
# function(keyword=value)

# Keyword arguments are passed to functions after any required positional arguments.
# But the order of one keyword argument compared to another keyword argument does not matter.


# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""
    # these are called docstrings  used for documentation
    # its a good practice to use these whenever we write a function and specify what the function does

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(is_leap(2050))
print(days_in_month(2017, 2))
# False
# 28
