# special methods or dunder methods are used for operator overloading
# for ex , 1+2 is  3 , 'a' +'b' = 'ab' so operator operates based on objects ,
# so this is done with the help of dunder methods ,
# and if we try to print print(emp_1) it ll give us vague notation reference of class ,
# if want to customise it or change it ot our convenience we can use dunder method
import pytz as pytz


class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1 + emp_2)  # Employee.__add__(emp_1,emp_2)

print(emp_1.__repr__())
print(emp_1.__str__())
print(repr(emp_1))
print(str(emp_2))
print(emp_1)  # if dunder str method is not implemented , it ll check for dunder repr

print(len(emp_1))
print(emp_1.__len__())

# A class can implement certain operations that are invoked
# by special syntax (such as arithmetic operations or subscripting and slicing) by defining methods with special names.
# This is Python’s approach to operator overloading,
# allowing classes to define their own behavior with respect to language operators.

#
# object.__repr__(self)
# Called by the repr() built-in function to compute the “official” string representation of an object.
# If at all possible, this should look like a valid Python expression that could be used to recreate an object
# with the same value (given an appropriate environment).
# If this is not possible, a string of the form <...some useful description...> should be returned.
# The return value must be string object. If a class defines __repr__() but not __str__(), then __repr__() is also used
# when an “informal” string representation of instances of that class is required.
# This is typically used for debugging, so it is important that the representation is information-rich and unambiguous


#
# object.__str__(self)
# Called by str(object) and the built-in functions format() and print() to compute the “informal”
# or nicely printable string representation of an object. The return value must be a string object.
#
# This method differs from object.__repr__()
# in that there is no expectation that __str__() return a valid Python expression:
# a more convenient or concise representation can be used.
#
# The default implementation defined by the built-in type object calls object.__repr__().


# ex from date tiem module


# __str__ vs __repr__

a = [1, 2, 3]
b = 'Sample string'

print(str(a), repr(a))
print(str(b), repr(b))

#    [1, 2, 3]
#    [1, 2, 3]
#    Sample string
#   'Sample string'

# not very clear

# goal of __repr__ is to be unambiguous
# goal of str is to be readable

import datetime
import pytz

a = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

b = str(a)

print('str(a): {}'.format(str(a)))
print('str(b): {}'.format(str(b)))

print()

print('repr(a): {}'.format(repr(a)))
print('repr(b): {}'.format(repr(b)))

print()
