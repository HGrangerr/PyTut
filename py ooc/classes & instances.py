# classes - logically group data and funcs together in a way its esy to manage
# and reuse and build upon
# we ll call it attributes and methods
# each class obj is gonna have specific attributes and methods
class Student:
    pass


# if we leave it empty we l l get an error , so
# if we wanna skip it , or write it later , declare it as pass

stu1 = Student()
stu2 = Student()


# diff btw classes and instance variables
# classes are blueprint for creating instances

stu2.first = 'Rach'
stu2.second = 'B R'

stu1.first = 'Aara'
stu1.second = 'B R'

print(stu2, stu1)


# <__main__.Student object at 0x02D52FE8>
# <__main__.Student object at 0x02D52FB8>

class Employee:
    def __init__(self, first, second, pay=0):      # constructor
        self.first = first
        self.second = second
        self.pay = pay
        self.email = first + '.' + second + '@company.com'

    def print_name(self):
        return '{} {}'.format(self.first, self.second)


emp_1 = Employee('Rach', 'BR')
print(emp_1.email)
print(emp_1.pay)
print(emp_1.print_name())

# Rach.BR@company.com
# 0
# Rach BR


print()
# print with no arguments can be used to print blank line

emp_2 = Employee('Aara', 'BR', 50000)
print(emp_2.email)
print(emp_2.pay)
print(emp_2.print_name())

# Aara.BR@company.com
# 50000
# Aara BR