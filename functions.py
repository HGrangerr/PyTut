# functions
# functions are a set of instructions packaged together for doing specific tasks
# to create a func in py,
# we need to use the keyword def,which maybe stands for definition , and then give the name of the function

def func_one():
    pass


# do nothing func , it doesnt throw an error , use this if we want to provide functionality  it later

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
# ex wif we have some text which is repeating itself in our program for n times,
# we can put it in a func and use that n times
# this is helpful in situations where if we want to make any changes to the code ,
# we dont have to change all n lines but instead change in that one function
# so functions alllow us to put code which does a specific thing in a func, single location ,
# and use it multiple times, and if we want to change , change it once , inside the func
# , and change is reflected everywhere
# so this is called DRY (Don't Repeat Yourself)


def func_hello():
    return 'hello'


func_hello()

# does nothibg

print(func_hello())
# hello

# so ypu  can think of a func as some machine which takes in input and procuses some output
# or a blackbox , you dont need to know hows its doing whats it doing

# we can treat the return value as the data type itself
# ex if a func returns a strin g, we can apply all methods of string on i t
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

def func_hello(msg, name='yo'):
    return '{} {} ! ,welcome'.format(msg, name)


print(func_hello('hi'))

# hi yo ! ,welcome

print(func_hello('hi', name='corey'))
# hi corey ! ,welcome
print(func_hello('hi', 'rach'))
# hi rach ! ,welcome
