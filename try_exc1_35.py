
def calc_salt(salt):
    try:
        # x = int(input())#Zanosim
        salt = int(salt)/1000
        return salt
    except ValueError as e:
        print(e)
        return 0, 0

#         print(e)
#         return 0, 0
#     finally:
#         print('Finally close ...')
print(calc_salt(2000))
print(calc_salt('2000'))
print(calc_salt('abc'))
#
# # результаты вывода
# 20.0
# 20.0
# invalid literal for int() with base 10: 'abc'
# 0.0
# def get_value():
#     try:
#         x, y = map(int, input().split())#Zanosim cherez probel
#         return x, y
#     except ValueError as e:
#         print(e)
#         return 0, 0
#     finally:
#         print('Finally close ...')
# print(get_value())
