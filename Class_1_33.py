class Item:
    def __init__(self, name, price, quantity=0):

        self.__check(name, price, quantity)
        self.name = name
        self.price = price
        self.quantity = quantity
    def __str__(self):
        # print('str exists')
        return f'{self.name}, {self.price}, {self.quantity}'

    @staticmethod
    def __check(name, price, quantity):
        # try:

        if not isinstance(name, str):
            raise TypeError('name dolzhnobit str')

        if not isinstance(price, int):
            raise TypeError('price dolzhnobit int')

        if not isinstance(quantity, int):
            raise TypeError('quantity dolzhnobit int')

            # return self.__check(name, price, quantity)

        # except TypeError as e:
        #     print(e)

 # try:
 #        result = 0
 #        for n in nums:
 #            result += n
 #        return result
 #    except TypeError as e:
 #        print(e)
# from typing import Type, Any
# def isclass(cl: Type[Any]):
#     try:
#         return issubclass(cl, cl)
#     except TypeError:
#         return False



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
#
# obj1=Item(1)
# obj2=Sub(1,2)
# obj3=SubSub(1,2,3)

print(Item('phone', 18000, 5))
# Item(phone, 18000, 5)  # работает метод __str__
#
# print(Item(18000, 'phone', 5))
# TypeError: Название товара должно быть строкой.
#
# print(Item('phone', '18000', 5))
# TypeError: Цена товара должна быть числом.
#
#
# >>> print(Item('phone', 18000, 5.5))
# TypeError: Количество товара должно быть целым числом
#
#
# class Item:
#     @classmethod
#     def is_integer(num):
#         if isinstance(num, float):
#             return num.is_integer()
#         elif isinstance(num, int):
#             return True
#         else:
#             return False
# x = Item.is_integer(8.8)
# print(x)