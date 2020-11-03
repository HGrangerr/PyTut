class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')

emp_1.first = "Rach"
print(emp_1.fullname())
print(emp_1.email)


# Rach Smith
# John.Smith@company.com

# now if i change the fullname of an employee , only the full name will change , not the email ,
# so one obvious solution that comes to mind is that to write one more method like fullname method for email
# which fetches the firstname, lastname and creates email

# but that would require change of code of all ppl using our class
# so instead u can add the @property at the beginning of method , then u could call the function without using ()
# u could also do the same for fullname


class employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


# now u could call the fullname without parenthesis


emp_2 = employee("aara", "br")
print(emp_2.fullname)
print(emp_2.email)


# aara br
# aara.br@email.com

# but cant set the fullname so can write  setter

class Employee1:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_3 = Employee1("", "")

emp_3.fullname = "Corey Schafer"

print(emp_3.first)
print(emp_3.email)
print(emp_3.fullname)

del emp_3.fullname  # this would call @fullname.deleter

# Corey
# Corey.Schafer@email.com
# Corey Schafer
# Delete Name!
