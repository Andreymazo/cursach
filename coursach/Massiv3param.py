z = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
# z = [[0,0,1], [1,0,3], [1,1,5], [2,0,7], [2,1,9], [2,2,11], [3,0,13], [3,1,15], [3,2,17], [3,3,19], [4,0,21], [4,1,23], [4,2,25],[4,3,27], [4,4,29]]
def append_z(value):
    ####### nom_ryada - 1########
    ####### nom_v_stroke - 2#####
    # value_nech = []
    # n = int(input('Введите число, до которого принимаем нечечетные числа'))
    #
    # for i in range(0, n):
    #     if i % 2 != 0:
    #         value_nech.append(i)  # Сформируем список из нечетных чисел

    value_new = []#Принимаем массив по условию задачи
    nom_ryad = 0
    nom_v_stroke = 0
    for i in value:
        if nom_ryad > nom_v_stroke:
            value_new.append((nom_ryad, nom_v_stroke, i))
            nom_v_stroke += 1

        elif nom_ryad == nom_v_stroke:
            value_new.append((nom_ryad, nom_v_stroke, i))
            nom_v_stroke = 0
            nom_ryad += 1

    # value_0 = int(input('Vvedite 0'))# 0
    # if value_0 == 0:#, ставим его в конец
    #     value_new.append((nom_ryad,nom_v_stroke+1, value_0))
    k = int(input('vvedite nomer ryada, na kotorom schitat summu nech chisel'))
    kk=[]
    nom_ryad = 0
    nom_v_stroke = 0
    print(value_new)
    for i in value_new:
        if i[0] == k:
            kk.append(i)#Sobrali nashi chleni
        #print(kk)
    tt = []
    for i in kk:
        tt.append(i[2])
    print(sum(tt))###125 Vse rabotaet
    # return value_new, nom_v_stroke, nom_ryad, print(value_new, nom_v_stroke, nom_ryad)
append_z(z)