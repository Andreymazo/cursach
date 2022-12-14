import csv
from itertools import islice
from operator import itemgetter
import pprint

##############Сортируем по PCLN и по 2013-07-12 файлы для проверки
# all_stocks_5yr.csv  output_sorted_PCLN (отсортирован пандой, встроенный поиск только 20000 строк обрабатывает
# за 45 секунд. Записывает отсортированное в файл out.csv. на 102 строчке можно раскомментировать принт new
# это отсортированный словарь по нашему поиску, без панды. функция isliced сечас держит 10 значений, можно
# добавить без фанатизма и проверить, что все рабоатет (к конечному new отношения не имеет)
# #########################
def dec_cache(func):
    cache = {}

    def wrapper(dic):
        if dic[0] in cache:
            return dic[0]
        value = func(dic)
        cache[0] = value
        return value

    return wrapper


@dec_cache
def sort_smth(dic):  ###Минимальное число справа и проверка на отсортированность counter = 0
    # counter счетчик заменыб если нуль, то отсортирован
    #####Сначала пробежим и найдем наименьший элемент
    result = False
    while not result:  # Сюда надо снова подать будет список после его сортировки пополам, т.е. high из функции f_3

        index = 0
        counter = 0
        for i in range(len(dic)-1):
            try:
                # print(high)
                # if high[index] < high[index + 1] and index==len(high):
                #     index = 0
                if dic[index] < dic[index + 1]:
                    dic[index], dic[index + 1] = dic[index + 1], dic[index]  ###Наименьший элемент в конце цикла окажется на последнем месте
                    index += 1
                    counter += 1
                    # print(counter, high)
                elif dic[index] > dic[index + 1]:
                    index += 1
                elif dic[index] == dic[index + 1]:
                    #     ost.append(high[index])  ##Дубликат заносим в ost
                    #     high.remove(high[index])  ##Дубликат убираем
                    index += 1
                #     counter += 1
                if counter == 0 and index == len(dic) - 1:  ##Услловие выхода из прогграммы, весь список отсортирован, ni odnogo izmenenia ne proizoshlo
                    # print(counter, high)
                    result = True  ## V etoi tochke dolzhen bit otsortirovannii spisok high i spisok ost s duplicarami
                    break  # No pochemu to go konca nedosortirovivaet

            except IndexError:
                pass
            continue

    return dic


def select_sorted(sort_columns='high', order='asc', limit=10, filename='dump.csv', group_by_name=False):
    high_lst = []
    with open('all_stocks_5yr.csv', 'r', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        group_by_name = []
        for row in reader:## Sozdali spisok is 10 elementov
            if len(high_lst) < limit:
                high_lst.append(row[sort_columns])
                group_by_name.append(row['Name'])

            else:
                break
        high_lst = [float(x) for x in high_lst]## pereveli iz str fo float
        group_by_name.sort()##Tut ispolsuu sort nechestno
        get_columns = itemgetter('date', 'open', 'high', 'low', 'close', 'volume', 'Name')
        Cache = {}

        with open('all_stocks_5yr.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            index_1 = 0
            high_lst = [float(x) for x in high_lst]
            sort_smth(high_lst)#sortiruem
            high_lst = [str(x) for x in high_lst]#Perevodim obratno v str
            # ['13.6', '13.95', '14.26', '14.51', '14.56', '14.61', '14.94', '14.96', '15.01', '15.12']
            for row in islice(reader, limit):  # first 10 put into Cache
                Cache[high_lst[index_1]] = get_columns(row)  ##V kachestve kluchei znachenia high iz high_lst
                index_1 += 1

            ## Obrashaemsya k elementu kortezha v slovare Cache: Cache[index_1]['high'] esli sovpal, to kortezh celicom stavim na 1 mesto
            new = {}
            index_1 = 0
            index_2 = 0
            for k in Cache:
                for v in Cache:
                    if k == Cache[v][2]:
                        new.update({k: Cache[v]})
                        index_1 += 1
                    elif k != Cache[v][2]:
                        index_1 += 1
                        index_2 += 1
                        # print(new)
            #pprint.pprint(new, width=100)#slovar new otsortirovan
            return new
Cache = select_sorted(sort_columns='high', limit=10, order='desc', filename='dump.csv', group_by_name=True)


##############U nas est spisok, teper nado svormirovat slovar i otsortirovat ego po etomu spisku


def search_1(array, nomer, element):
    index_1 = 0
    for i in range(len(array)):
        index_1 += 1
        if array[index_1][nomer] == element:
            return index_1#, print('1 index', index_1)##Nahodim 1 index PCLN

#1 index 440061
def search_1_dlya_2(array, nomer, element, index_1_2):

    for i in range(len(array)):
        index_1_2 += 1
        if array[index_1_2][nomer] == element:
            return index_1_2, print('1 index_1_2', index_1_2)##Nahodim 1 index PCLN

def search_Posled_dlya2(array, nomer, element, index_1):
        index_P = len(array) - 1
        # index_P_dlya_2 = 0
        print('index_P', index_P, 'index_1' , index_1)
        for i in range(len(array)):
                index_P -= 1
                # print(array[index_1+index_P])
                if array[index_1+index_P][nomer] == element:
                    index_P_dlya_2 = index_1 + index_P
                    return index_P_dlya_2, print('Posled index', index_P_dlya_2)##Nahodim Posled index PCLN##Posled index 440167


# Введите для поиска сам второй параметр2013-07-12

def search_Posled(array, nomer, element):
    index_P = len(array)-1
    for i in range(len(array)):
        index_P -= 1
        if array[index_P][nomer] == element:
            return index_P#, print('Posled index', index_P)##Nahodim Posled index PCLN
#Posled index 441319

def poisk(limit=10):###Ishem PCLN 2017-08-08(takogo znacheniya net)####'2013-02-12'
    global srez
    name = []
    get_columns = itemgetter('date', 'open', 'high', 'low', 'close', 'volume', 'Name')
    with open('output_sorted_PCLN') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name.append(row['Name'])##Poluchaem spisok name, po nemu budem potom sortirovat(obrashatsya)
            # print(len(name))
    mass = {}


            ##Nuzno mass sdelat polnim 619040, a ne 440062
    with open('output_sorted_PCLN') as csvfile:  ##Sortiruem po imeni PCLN Len obshii 619040
        reader = csv.DictReader(csvfile)
        index_1 = 0
        # name = [str(x) for x in name]## Sozdali spisok 619040 elementov
        counter = 0
        for row in islice(reader, 619040):  #
            mass[index_1] = get_columns(row)  ##V
            index_1 += 1

        # print(len(mass))##619040
    ####################Ishe 1 i posled index PLCN#####################
    vvod_nomer = int(input('Введите номер параметра для поиска согласно date = 0, open=1, high=2, low = 3, close=4, volume=5, Name=6'))
    vvod_parametr = str(input('Введите для поиска сам параметр'))
    index1 = search_1(mass, vvod_nomer, vvod_parametr)
    # print('index1=', index1) # index1= 440061

    indexp = search_Posled(mass, vvod_nomer, vvod_parametr)
    # print(indexp)#441319
    #440061
    #441319
    ###############Nahodim srez количество одинаковых####################
    new = {}
    print(len(mass))#619040
    index = 0
    for i in range(len(mass)):
        index += 1
        if indexp > index > index1:
           new[index]=mass[index]
    #print(len(new))#1257
    #print(new[441413])
    #########################################
    print(f'Элементов с параметром {vvod_parametr} ', len(new), ' штук')
    vvod_nomer_2 = int(input('введите номер номер параметра для вторичного поиска согласно date = 0, open=1, high=2, low = 3, close=4, volume=5, Name=6 из нового списка'))
    vvod_parametr_2  = str(input('Введите для поиска сам второй параметр'))
    # index1_f_dlya_2 = index1
    index_1_2, gg = search_1_dlya_2(new, vvod_nomer_2, vvod_parametr_2, index1)#index1_f_dlya_2
    #print('Певрый индекс dlya_2 = ', gg)#(440167, None)
    # print('Последний индекс dlya_2', index1)
#
    index_P_dlya_2, g = search_Posled_dlya2(new, vvod_nomer_2, vvod_parametr_2, index1)
    #print('Последний индекс dlya_2 index1_f_dlya_2', g)
    #print(indexp)#(440167, None)

    ####################### Soberem vse povtorivsh elementi, v nashem sluchae ih odin##############
    f = []
    idex = index_1_2
    for i in new:
        if index_1_2 <= idex <= index_P_dlya_2:
            f.append(new[idex])
            idex += 1
    print(f)#new[440167]
    # 1257 print (idex)
    ###########################Выводим в csv файл #####################
    data = f
    with open('out.csv', 'w+') as csvfile:
        for row in f:
            csvfile.writelines(row)

poisk()