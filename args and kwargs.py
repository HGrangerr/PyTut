# The special syntax *args in function definitions in python
# is use0d to pass a variable number of arguments to a function.
# It is used to pass a non-keyworded, variable-length argument list.

def info(*args, **kwargs):
    print(args, kwargs)


# *args can take in any iteratable objects as argument
# kwargs can take a dictionary
# u can use anything in place of args , but args is the convention
# * is called unpacking operator (*)

info()
# () {}


# TODO testing todo

info(1, 2, 3, name='Rach', age=22)

# (1, 2, 3)  so args is the tuple with our positional arguments
# {'name': 'Rach', 'age': 22}
# kwargs is the dictionary with our keyword values
list = [1, 2, 3]
informa = {'name': 'Rach', 'age': 22}

info(list, informa)
# ([1, 2, 3], {'name': 'Rach', 'age': 22}) {}
# in this both are considered as positional elements ,so creates an empty dictionary

# instead if we pass in * and ** then it wil unpack those values and pass it in individually

info(*list, **informa)
# (1, 2, 3) {'name': 'Rach', 'age': 22}


