# Создадим папку temp1, если ее нет и сложим туда разделенный на части наш файл

import os
import shutil
from datetime import datetime

import sortirovka_mal_filov
from sortirovka_mal_filov import sort_mal_fil


def rm_r(path):
    print("Udaliaem ...")
    if not os.path.exists(path):
        return
    if os.path.isfile(path) or os.path.islink(path):
        os.unlink(path)
    else:
        shutil.rmtree(path)

import csv
def zapis(data_,file_counter_):
    with open(f'{filepath_1}/newfile_{file_counter_}.csv', 'w+') as ff:#, newline=''
        # writer = csv.writer(ff)#Для записи данных есть функция 'writer()' Нам не подошла почему-то
        # writer.writerow(i)
        ff.writelines(data_)

def devider():
    line_counter = 0
    file_counter = 0

    with open('coursach/data/all_stocks_5yr.csv') as f:
        header = next(f)
        data = [header]  # Поставили курсор на оглавление

        for i in f:
            if line_counter >= 100000:
                line_counter = 0
                file_counter += 1
                zapis(data, file_counter)
                # print("Here we are")
                data = [header]
            data.append(i)
            line_counter += 1
        file_counter += 1
        # file_counter += 1  # Дозаписываем остаток в 8ой файл
        if len(data) > 0:

            with open(f'{filepath_1}/newfile_{file_counter}.csv', 'w+', newline='') as ff:
                ff.writelines(
                    data)  #######Здесь у нас поделенный файл на несколько. Дальше соберем в один и походу сортируем
    return file_counter


if __name__ == "__main__":
    filepath_1 = 'temp1'
    filepath_2 = 'result_dir'

    if os.path.isdir(filepath_1):
        print('Est diretoria temp1')
    else:
        os.mkdir(filepath_1)
    if os.path.isdir(filepath_2):
        print('Est diretoria result_dir')
    else:
        os.mkdir(filepath_2)

    g = len(os.listdir(filepath_1))
    gg = len(os.listdir(filepath_2))
    devider()
    g = len(os.listdir(filepath_1))
    print(f'V direktorii temp1 {g} filov')
    sortirovka_mal_filov.sort_mal_fil(filepath_1,filepath_2)
    ff = int(input('Если все проверили, то можно удалять все файлы и папки? Нажмите 1 Если еще хотите посмотреть, то хм.. смотрите'))
    if ff == 1:
        rm_r(filepath_1)
        rm_r(filepath_2)
