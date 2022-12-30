# Создадим папку temp1, если ее нет и сложим туда разделенный на части наш файл

import os
import csv
from datetime import datetime

# os.remove() removes a file.
#
# os.rmdir() removes an empty directory.
#
# shutil.rmtree() deletes a directory and all its contents.
filepath = 'temp1'
# 'C:\Users\user\PycharmProjects\Cursach'
#  try:
#     os.path.exists(filepath)
#     print("Nachalo 1")
#     # os.rmdir(filepath)#Для удаления целых деревьев каталогов можно использовать функцию shutil.rmtree().
#     #os.rmdir(filepath,  dir_fd=None)#dir_fd=None - int, дескриптор каталога,   *,
#  except FileExistsError as e:
#     print("Nachalo 2 Est diretoria temp1'")
#
if os.path.isdir(filepath):
    print('Est diretoria temp1')
else:
    os.mkdir(filepath)
    # >> > path = 'test_dir'
    # # Создадим каталог
    # >> > os.mkdir(path, 0o774)
    # >> > os.path.isdir(path)
    # # True
    #
    # # Удалим каталог
    # >> > os.rmdir(path)
    # >> > os.path.isdir(path)
    # # False

# if os.path.isfile('data/temp/')
# with open('coursach/data/all_stocks_5yr.csv', 'r', newline='') as f:
# result = csv.reader(f, delimiter=',')#Для чтения файлов используется функция 'reader()', которая возвращает объект для итерации.

# ['2015-03-27,67.24,67.525,66.71,66.98,453740,EXR']
# ['2015-03-30,67.22,68.43,67.01,68.26,567490,EXR']
# ['2015-03-31,68.21,68.52,67.315,67.57,1099200,EXR']
# ['2015-04-01,67.57,67.84,66.625,67.34,599922,EXR']
# ['2015-04-02,67.34,68.38,67.21,67.87,935540,EXR']
# for i in result:
#     print(i)
def zapis(data_,file_counter_):
    with open(f'{filepath}/newfile_{file_counter_}', 'w', newline='') as ff:
        # writer = csv.writer(ff)#Для записи данных есть функция 'writer()' Нам не подошла почему-то
        # writer.writerow(i)
        ff.writelines(data_)


line_counter = 100000
file_counter = 0

with open('coursach/data/all_stocks_5yr.csv') as f:
    header = next(f)
    data = [header]  # Поставили курсор на оглавление
    for i in f:
        if line_counter >= 100000:  # Почему 1ый файл пустой?????
            file_counter += 1
            line_counter = 0
            zapis(data, file_counter)
            # print("Here we are")
            data = [header]
        data.append(i)
        line_counter += 1
    file_counter += 1
    # file_counter += 1  # Дозаписываем остаток в 8ой файл
    if len(data) > 0:

        with open(f'{filepath}/newfile_{file_counter}', 'w+', newline='') as ff:
            ff.writelines(
                data)  #######Здесь у нас поделенный файл на несколько. Дальше соберем в один и походу сортируем
g = len(os.listdir(filepath))
print(f'V ney {g} filov')
# for i in range(g):
#     with open(f'{filepath}/newfile_{i}', 'r') as file_i:
#         data = csv.DictReader(file_i)## Schitali s 1ogo fila
#     open(f'{filepath}/resultfile', 'w+') as resultfile:
#     result_data = csv.DictWriter(resultfile, [*data.fieldnames])
#     result_data.writeheaders()
