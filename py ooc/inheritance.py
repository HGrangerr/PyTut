# last classes we created this employee class , now  we can create subclasses for it ,
# inheritance means inheriting the attributes and methods from a parent class ,
# reuse the functionality of parent class , overriding / reuse and add the additional functionality
# without affecting the parent class

# or used to create a specific type fof parent class
# ex employee is parent of dev and managers

# here im creatig a subclass called dev  and keep it empty , yet when i create obj of thta type , theres no error
# we get the output ,
# so all of the functionality from the parent class is getting inherited


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


class Dev(Employee):
    pass


dev_1 = Dev('Corey', 'Schafer', 50000)
dev_2 = Dev('Test', 'Employee', 60000)

print(dev_1.email)
print(dev_2.email)


#
# Corey.Schafer@email.com
# Test.Employee@email.com


# so what really happens here is that py is gonna search for init method ,
# but its not gonna find it the

# dev class so searches it in  the parent class , this is called method resolution order
# we can know more about it using help() function
#
# print(help(Dev))

# Help on class Dev in module __main__:
#
# class Dev(Employee)
#  |  Dev(first, last, pay)
#  |
#  |  Method resolution order:  its the places in which the py searches
#                                for attributes and methods and in this order

#  |      Dev
#  |      Employee
#  |      builtins.object
#  |
#  |  Methods inherited from Employee:
#  |
#  |  __init__(self, first, last, pay)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |
#  |  apply_raise(self)
#  |
#  |  fullname(self)
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors inherited from Employee:
#  |
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |
#  |  __weakref__
#  |      list of weak references to the object (if defined)
#  |
#  |  ----------------------------------------------------------------------
#  |  Data and other attributes inherited from Employee:
#  |
#  |  raise_amt = 1.04
#
#
# so now if i had t change te raise_amt ,  you can specify it in the beg of subclass
# , this wont the affect the parent class and its members
# again when i call the methods its gonna search the attributes in the same order

class Dev(Employee):
    raise_amt = 1.15

    def __init__(self, first, last, pay, yrs_exp=0, langs=None):

        # Employee.__init__(self, first, last, pay)
        super().__init__(first, last, pay)
        self.yrs_exp = yrs_exp
        if langs is not None:
            self.langs = langs
        else:
            self.langs = []


dev_1 = Employee('Corey', 'Schafer', 50000)
dev_2 = Dev('Test', 'Employee', 60000)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print(dev_2.pay)
dev_2.apply_raise()
print(dev_2.pay)


# 50000
# 52000
# 60000
# 69000

class dev(Employee):
    raise_amt = 1.15

    def __init__(self, first, last, pay, yrs_exp=0, langs=None):

        # Employee.__init__(self, first, last, pay)
        super().__init__(first, last, pay)
        self.yrs_exp = yrs_exp
        if langs is not None:
            self.langs = langs
        else:
            self.langs = []


developer_1 = dev('Corey', 'Schafer', 50000, 0.5)
developer_2 = dev('Test', 'Employee', 60000, 5, ['py', 'java'])


class Manager(Employee):
    list1 = [1, 2, 3]

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

    def print_emps_as_str(self):
        # print(self.employees)  # wont work, this is a list containing objects ,
        # print(self.employees.print_name())  # need to use in a for loop and then call the function on each object
        print(self.list1)  # works, this is a list containing vars


mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)

mgr_1.print_emps()
mgr_1.string_emps()

print(Manager.list1)
print(mgr_1.list1)

# isinstance()
#  issubclass()

# example from HTTPException() class
