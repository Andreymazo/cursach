import os
import csv
from datetime import datetime
from itertools import islice
from sorter import quick_sort
from operator import itemgetter
# os.remove() removes a file.
#
# os.rmdir() removes an empty directory.
#
# shutil.rmtree() deletes a directory and all its contents.

def sort_mal_fil(filepath_11, filepath_22):
    global vved_nomer
    filepath_11 = 'temp1'
    filepath_22 = 'result_dir'
    g = len(os.listdir(filepath_11))
    gg = len(os.listdir(filepath_22))
    print(f'V ney {g} filov')
####################Probuem bez slovarya###########
# for i in range(1,2):
#     print(f"Sortirovka po high,  file: {i}")
#     with open(f'{filepath}/newfile_{i}.csv', 'r', encoding='utf8') as f:
#         data = csv.DictReader(f, fieldnames=None, delimiter=',')
#         dic = []
#         for i in data:
#             dic.append(i)
##print(dic)##v kazhdoy strochke fieldsnames#####################

#######################################Sortiruem malenkie file#############################
    try:
        vved_nomer = int(input('Введите номер по которому сортировать: date 0, open 1, high 2, low 3, close 4, volume 5, Name 6'))
    except TypeError or ValueError:
        print('Введите число от 0 до 6')

    for i in range(1,g+1):
        print(f"Sortirovka po {vved_nomer},  file: {i}")
        with open(f'{filepath_11}/newfile_{i}.csv', 'r', encoding='utf8') as f:
            data = csv.DictReader(f, fieldnames=None, delimiter=',')
            dicc = {}
            index = 0
            get_columns = itemgetter('date', 'open', 'high', 'low', 'close', 'volume', 'Name')## Ubiraem fieldnames
            for ii in data:#islice(data, 1000):##Perevedem v dict i sortiruem
                dicc[index] = get_columns(ii)  ##V kachestve kluchei znachenia high iz high_lst
                index += 1
            # print(dicc)
            quick_sort(dicc, vved_nomer)
            dic = []
            for k, v in dicc.items():
                dic.append(dicc[k])

            with open(f'{filepath_22}/result_file_{i}.csv', 'w+', newline='') as ff:#Nado dic zapisat v novii file
                # fieldnames = ['date', 'open', 'high', 'low', 'close', 'volume', 'Name']
                # result_data = csv.DictWriter(ff, fieldnames=fieldnames)#Tolko chtobi postavit nazvanie kolonok 3 strochki
                # result_data.writeheader()###No dlia sortirovki nam poka ne nado
                writer = csv.writer(ff)#Zanosim v file
                writer.writerows(dic)
#################Soberem v odin i otsortituem i ego####################
    with open(f'{filepath_22}/result_file',
              'a', newline='') as resultfile:  ##Vse ravno s nachala pishet, no potom s 400 000 norm, 1 file otdelno zapisat nado
        fieldnames = ['date', 'open', 'high', 'low', 'close', 'volume', 'Name']
        result_data = csv.DictWriter(resultfile, fieldnames=fieldnames)  # [*data.fieldnames]
        # file_i = open(f'{filepath}/newfile_{i}.csv', 'r', encoding='utf8')  # Ostalnie otkrivaem s mode 'a', pishet v konec fila
        for i in range(1, gg):
            print(f'Zapushen process : {i}')
            with open(f'{filepath_11}/newfile_{i}.csv', 'r', encoding='utf8') as file_i:
                data = csv.DictReader(file_i, delimiter=',')
                result_data.writeheader()
                for ii in data:
                    result_data.writerow(ii)

