my_list = [1, 2, 3, 4, 5]
print(my_list)

print(my_list[0:4:2])  # [start:end:step ]

# [1, 2, 3, 4, 5]
# [1, 3]
print(my_list[::-1])

# [5, 4, 3, 2, 1]


# sorting lists ,tuples and objects

# sort method is inplace, returns none
# sorted methods returns a sorted list,is not in place , works on lists , tuples, dictionaries (sort the keys)
# sort works only for list
# for descending order pass along with the list the parameter , reversed =True


tup = (1, 4, 7, 3, 42)
sorted_tup = sorted(tup, reverse=True)
print(sorted_tup, "\n", tup)

# [1, 3, 4, 7, 42]
# (1, 4, 7, 3, 42)
print(type(sorted_tup))

# <class 'list'>
listy = [-6, 5, -4]
print(sorted(listy))
# [-6, -4, 5]

print(sorted(listy, key=abs))
# [-4, 5, -6]

class Employee:

    def __init__(self, first, second, age, pay=0):  # constructor
        self.first = first
        self.second = second
        self.age = age
        self.pay = pay
        self.email = first + '.' + second + '@company.com'

    def print_name(self):
        return '{} {}'.format(self.first, self.second)

    def __repr__(self):
        return "Employee('{}','{}',{}, {})".format(self.first, self.second, self.age, self.pay)


emp_1 = Employee('Rach', 'BR', 29)
emp_2 = Employee('Aara', 'a', 33, 50000)
emp_3 = Employee('Aarabhi', 'yR', 45, 50000)

employees = [emp_1, emp_3, emp_2]


# sorted_emp = sorted(employees)  TypeError: '<' not supported between instances of 'Employee' and 'Employee'

def func_sort(Employee):
    # return self.first
    return Employee.age
    # return self.pay


sorted_emp = sorted(employees, key=func_sort)
# so this is gonna pass every emp through the key function and then sort according to that
print(sorted_emp)


# [Employee('Rach','BR',29, 0), Employee('Aara','a',33, 50000), Employee('Aarabhi','yR',45, 50000)]
