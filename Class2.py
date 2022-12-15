from _datetime import datetime as dt
#Для получения текущей даты и времени можно использвоать datetime.datetime.now()
class Task:


    def __init__(self, content):
        self.__content = content

    def __setitem__(self, key, value):
        print('Setitem exists')
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
        return f'{self.__content}) создано {dt.now()}'
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
# a=Task('5')
# bool(a)
# if a:
#     print('yes')

todo_list = []
#
todo_list.append(Task('Сделать домашку'))
todo_list.append(Task(''))
todo_list.append(Task('Сделать домашку'))
todo_list.append(Task(''))
print(todo_list)
non_empty_tasks = [item for item in todo_list if item]
print(non_empty_tasks)
# [Сделать домашку(создано 2022 - 12 - 08 12: 21:16), Сделать домашку(создано 2022 - 12 - 08 12: 21:16)]

print(len([item for item in todo_list if not item]))