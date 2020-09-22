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

    # Employee.raise_amt= 1.20
    @classmethod
    def set_raise_amt(cls, amt):
        cls.raise_amt = amt

    @classmethod
    def from_string(cls, emp_str):  # alternative constructors
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)  # returns the cls id or whatvr

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Aarabhi', 'BR', 80000)

# Employee.raise_amt= 1.20
# print(emp_1.raise_amt, Employee.raise_amt)  # 1.2 1.2


Employee.set_raise_amt(1.15)
# emp_1.set_raise_amt(1.15)
print(emp_1.raise_amt, Employee.raise_amt)  # 1.15 1.15

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

first, last, pay = emp_str_1.split('-')

# new_emp_1 = Employee(first, last, pay)
new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

# @staticmethod  has a logical connection with the employee class
# but doesnt have any connection with the instances(emps) or class vars

# easy way to figure out whether method should static or cls or self is
# if were not using the inst vars or the class vars anywhere inside the func then it means its gotta be a static method
# coz static methods don't operate on instances or classes

import datetime

my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))
