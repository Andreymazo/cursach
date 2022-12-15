from _datetime import datetime as dt
#Для получения текущей даты и времени можно использвоать datetime.datetime.now()
class Task:

    def __init__(self, content):
        self.__content = content

    def __setitem__(self, key, value):
        print('Setitem exists Task')
        self.__content[key] = value
    def __getitem__(self, item):
        print('getitem exist')
        return self.__content[item], dt.now == self.__content
    def __keys(self):
        return (self.__content)

    def __eq__(self, other):
        if isinstance(other, Task):
            return self.__keys() == other.__keys()  # Sravnivaem dve stringi model,color dvuh ekzempliarov classa Cars
        return NotImplemented

    def __hash__(self):
        return hash(self.__keys())

    def __str__(self):
        print('str')
        return f'{self.__content} создано {dt.now()}'
    def __len__(self):
        print('len exist')
        return len(self.__content)
    def __repr__(self):
        print('repr exists')
        return str(f'{self.__content} , создано {dt.now()}')
    def __bool__(self):
        if not len(self.__content):
            print('bool exists')
        return bool(len(self.__content))

class TodoList:

    def __init__(self):
        self.tasks = [0, 1]
        self.counter = 0

    def __setitem__(self, key, value):
        print('setitem exists', key, value)
        self.tasks[key] = value

    # def __getitem__(self, item):
    #     print('getitem exists')
    #     return self.tasks[item]

    def __repr__(self):
        print('repr todolist')
        return str(self.tasks)
    def __delitem__(self, key):
        print('del exists')
        del self.tasks[key]
    # def __iter__(self):
    #     self.tasks=self.start-self.step
    #     return self
    def __next__(self):
        if self.counter < len(self.tasks):
            result = self.tasks[self.counter]
            self.counter += 1
            return result
        else:
            raise StopIteration

todo_list = TodoList()
todo_list[0] = Task('Сдать домашку')
todo_list[1] = Task('Выпить кофе')

next(todo_list)#TypeError: 'TodoList' object is not an iterator
#Сдать домашку (создано 2022-12-08 12:34:33)
next(todo_list)
#Выпить кофе (создано 2022-12-08 12:34:33)

# todo_list = TodoList()
# todo_list[0] = Task('Сдать домашку')
# todo_list[1] = Task('Выпить кофе')
# print(todo_list)
# # [Сдать домашку (создано 2022-12-08 12:34:33), Выпить кофе (создано 2022-12-08 12:34:33)]
# #
# print(todo_list[0])
# # Сдать домашку (создано 2022-12-08 12:34:33)
# #
# del todo_list[0]
# print(todo_list)
# # [Выпить кофе (создано 2022-12-08 12:34:33)]