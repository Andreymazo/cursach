# class Employee:
#
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#         self.email = first + '.' + last + '@gmail.com'
#
#     def fullname(self):
#         return f'{self.first} {self.last}'

class Employee:
    __slots__ = ('first', 'last')

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):#Tak rabotaet property
        return '{}.{} @email.com'.format(self.first, self.last)
    @property
    def fullname(self):
        return '{}.{}'.format(self.first, self.last)
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    @fullname.deleter
    def fullname(self):
        print('Delete Name')
        self.first = None
        self.last = None


    def setter(self, first, last):
        self.first = first
        self.last = last


    # дальше новый код

emp_1 = Employee('John', 'Smith')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
    # John
    # John.Smith@email.com
    # John Smith

emp_1.fullname = "Corey Schafer"
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
    # # Corey
    # # Corey.Schafer@email.com
    # # Corey Schafer
    #
del emp_1.fullname
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
    # None
    # None.None@email.com
    # None None

