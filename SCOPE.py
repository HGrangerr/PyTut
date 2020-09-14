'''legb
local , enclosing , global , built in
whenever python needs to access a variable it first checks the local scope ,
 if theres nothing , then checks  enclosing , global , then builtin variable '''

x = 'global x'  # global coz its in the main body


def test():
    y = 'local y '
    print(y)


test()  # local y


def test1():
    y = 'local y '
    print(y, x)


test1()  # local y  global x


# first checks the local scope ,
# if theres nothing , then checks  enclosing , global , then builtin variable

def test2():
    x = 'local x '
    print(x)


test2()  # local x
print(x)  # global x


# so not overridden , it has created a sep var in its stack ,
# and local var vanishes whenever the func call ends

# now, what if we wanted too work with global w=var and use it in a func

def test_global():
    global x
    x = 'local x '
    print(x)


test_global()  # local x
print(x)  # local x


# we can do this even without having to declare the x in the main scope

def test_global1():
    global y
    y = 'local y '
    print(y)


test_global1()
print(y)

# local y
# local y


# arguments als0oc oe under local scope
#   builtins
# py has a set of builtin funcs and vars
# , it follows legb rule so u can override it if needed
# ex : min is a func that takes a itr=erable as argument and returns the min among them
# u can override it (legb)
# u can see builtin vars in this


import builtins

print(dir(builtins))

# [mostly errors +  '__build_class__', '__debug__', '__doc__',
#  '__import__', '__loader__', '__name__', '__package__', '__spec__',
#  'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray',
#  'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright',
#  \'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec',
#   'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
#   'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter',
#   'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next',
#   'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range',
#   'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod',
#   'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

# enclosing - local scope of enclosing func
# any changes to local wont affect outside
# but , if we declare the var in inner function as a nonlocal var,
# just as we declared it global inside a func
# then the enclosing value will bbe used and overridden

x = 'global x'


def outer():
    x = 'outer x'

    def inner():
        nonlocal x
        x = 'inner x'
        print(x)

    inner()
    print(x)


outer()
print(x)

# inner x
# outer x
# global x , if nonlocal keyword is not use d

# if used
# inner x
# inner x
# global x
