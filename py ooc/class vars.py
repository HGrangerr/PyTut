# last exercise , we learnt about classes and instances of classes
# these instances of classes have values that are unique to the instance , these are called instance variable

# there are another type of variable s, which are called class variables
# which are same for all the instances of the classes

# stuff that are common for all employees and not unique

# in this particular ex we have raise amount which is same for employees of the organisation

class Employee:

    def __init__(self, first, second, pay=0):  # constructor
        self.first = first
        self.second = second
        self.pay = pay
        self.email = first + '.' + second + '@company.com'

    def print_name(self):
        return '{} {}'.format(self.first, self.second)

    def pay_raise(self):
        self.pay *= 1.04


emp_1 = Employee('Rach', 'BR')
emp_2 = Employee('Aara', 'BR', 50000)

print(emp_2.pay)
emp_2.pay_raise()
print(emp_2.pay)


# 50000
# 52000.0

# so if wanna know what raise amt is its hidden  inside function and also diff to change the value of it when required,
# so better to create a class variable

class Employee:

    def __init__(self, first, second, pay=0):  # constructor
        self.first = first
        self.second = second
        self.pay = pay
        self.email = first + '.' + second + '@company.com'

    def print_name(self):
        return '{} {}'.format(self.first, self.second)

    raise_amt = 1.08

    def pay_raise(self):
        self.pay *= Employee.raise_amt
        # self.pay *= self.raise_amt


emp_3 = Employee('Aarabhi', 'BR', 80000)
print(emp_3.pay)
emp_3.pay_raise()
print(emp_3.pay)

# 80000
# 86400.0

print(Employee.raise_amt)
print(emp_3.raise_amt)
# 1.08
# 1.08


# print(raise_amt)
# NameError: name 'raise_amt' is not defined

# even though these are class variable , we cant access them without using self or class name
# because whenever we try to print out the attribute using particular instance of class
# its gonna first check if we have that instance has that var ,
#  if not it checks if the class has that var
# we can be sure of it by prnting namesapce

print(emp_3.__dict__)

# {'first': 'Aarabhi', 'second': 'BR',
# 'pay': 86400.0, 'email': 'Aarabhi.BR@company.com'}


print(Employee.__dict__)

# {'__module__': '__main__', '__init__': <function Employee.__init__ at 0x00E44190>, 'print_name':
# <function Employee.print_name at 0x00E44148>, 'raise_amt': 1.08, 'pay_raise':
# <function Employee.pay_raise at 0x00E44100>,
# '__dict__': <attribute '__dict__' of 'Employee' objects>,
# '__weakref__': <attribute '__weakref__' of 'Employee' objects>, '__doc__': None}


emp_3.raise_amt = 1.05
print(emp_3.__dict__)

# {'first': 'Aarabhi', 'second': 'BR',
# 'pay': 86400.0, 'email': 'Aarabhi.BR@company.com', 'raise_amt': 1.05}

# this would create another instance var in the emp_3 itself , so it would find
# raise amt in its  namespace itself so wouldn't go searching for it tn the class

emp_4 = Employee('Rachitha', 'BR')
emp_5 = Employee('Aara', 'Bhara', 50000)

print(emp_5.raise_amt, emp_4.raise_amt, emp_3.raise_amt)

# 1.08 1.08 1.05

# overriding the class var for a particular instance if we want to
emp_5.pay_raise()
emp_4.pay_raise()
emp_3.pay_raise()

print(emp_5.pay, emp_4.pay, emp_3.pay)


# 54000.0
# 0.0
# 93312.0


class employee:
    no_of_emps = 0


    def __init__(self, first, second, pay=0):  # constructor
        self.first = first
        self.second = second
        self.pay = pay
        self.email = first + '.' + second + '@company.com'

        employee.no_of_emps += 1

print(employee.no_of_emps)


emp_7 = employee('Rachitha', 'BR')
emp_8 = employee('Aara', 'Bhara', 50000)

print(employee.no_of_emps)

#
# 0
# 2
