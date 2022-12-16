class MyList(list):
    print('Rabotaet mag method')
    def __init__(self, input_list):
        self.input_list = input_list
        print('Rabotaet mag method')
        super(MyList, self).__init__(input_list)
        print('Rabotaet mag method')
    def __str__(self):#Dobavliaem dlia massovosti
        print('Rabotaet mag metod')
        return f'{self.input_list}'
    def __len__(self):
        print('Rabotaet mag method')
        return len(self.input_list)

# my_list = MyList([0, 1, 2])
# print(my_list)
lst = MyList(['Jone', 'Snow', 'Java'])

if not lst[2] == 'Python':
    lst[2] = 'Python'

print(lst)
print(len(lst))