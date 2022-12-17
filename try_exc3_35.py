class InvalidAgeError(Exception):#Если по заданию можно унаследоваться от Exception, то вроеде ничего делать и не надо больше
    pass
    # def __init__(self, age):
    #     self.age = age
    # def value_age(self, age):
    #     if age < 0 or age >= 120:
    #         raise InvalidAgeError("Извините, этот возраст не корректен ")
    #     else:
    #         print('')
    # def __str__(self):
    #     return self.age

try:
    age = int(input('Введите ваш возраст: '))
    if age < 0 or age >= 120:
        raise InvalidAgeError('Извините, этот возраст не корректен')
    print(f'Вам {age} лет')
except ValueError:
    print('Возраст должен быть числом')
except InvalidAgeError as e:
    print(e)


# Введите ваш возраст: 25
# Вам 25 лет
#
# Введите ваш возраст: 255
# Извините, этот возраст не корректен
#
# Введите ваш возраст: aa
# Возраст должен быть числом