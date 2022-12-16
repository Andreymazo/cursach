class Item:
    def __init__(self, name, price, quantity=0):

        self.__check(name, price, quantity)
        self.name = name
        self.price = price
        self.quantity = quantity
    def __str__(self):
        # print('str exists')
        return f'{self.name}, {self.price}, {self.quantity}'

    # @staticmethod
    def __check(self, name, price, quantity):
        # try:

        if not isinstance(name, str):
            raise TypeError('name dolzhnobit str')

        elif not isinstance(price, int):
            raise TypeError('price dolzhnobit int')

        elif not isinstance(quantity, int):
            raise TypeError('quantity dolzhnobit int')
#
class Phone(Item):
    def __init__(self, name, price, broken, quantity=0):#name, price, quantity=0,
        # Item.__init__(self)
        super().__init__(name, price, quantity)
        self.broken = broken
        # Item.__init__(self.name)
        # Item.__init__(self.price)
        # Item.__init__(self.quantity)


phone1 = Phone("iPhone 10", 500, 5, 1)
print(phone1)
# print(Item('phone', 18000, 5))
# print(Item(18000, 'phone', 5))

# class Computer():
#     def __init__(self, computer, ram, ssd):
#         self.computer = computer
#         self.ram = ram
#         self.ssd = ssd

# Если создать дочерний класс `Laptop`, то будет доступ
# к свойству базового класса благодаря функции super().
# class Laptop(Computer):
#     def __init__(self, computer, ram, ssd, model):
#         super().__init__(computer, ram, ssd)
#         self.model = model
#
#
# lenovo = Laptop('lenovo', 2, 512, 'l420')
#
# print('This computer is:', lenovo.computer)
# print('This computer has ram of', lenovo.ram)
# print('This computer has ssd of', lenovo.ssd)
# print('This computer has this model:', lenovo.model)



# class Item:
#     def __init__(self,a):
#         self.a=a
#
# class Sub(Item):
#     def __init__(self,a,b):
#         self.b=b
#         Item.__init__(self,a)
#
# class SubSub(Sub):
#     def __init__(self,a,b,c):
#        self.c=c
#        Sub.__init__(self,a,b)

