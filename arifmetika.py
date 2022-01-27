"""
Принимаем строку от пользователя и сделаем с ней арифметическую операцию
"""

spisok = list(input("Введите арифметическое выражение:  "))
act_list = ['+', '-', '*', '/']
# print(spisok)

for i in spisok:
    if i in act_list:
        border = spisok.index(i)
        actn = i

st_num1 = ''.join(spisok[:border])
st_num2 = ''.join(spisok[border + 1:])

if '.' not in st_num1:
    srez1 = int(st_num1)
else:
    srez1 = float(st_num1)

if '.' not in st_num2:
    srez2 = int(st_num2)
else:
    srez2 = float(st_num2)

if actn == '+':
    print(srez1 + srez2)
elif actn == '-':
    print(srez1 - srez2)
elif actn == '*':
    print(srez1 * srez2)
elif actn == '/':
    try:
        print(srez1 / srez2)
    except ZeroDivisionError:
        print('Деление на ноль')
