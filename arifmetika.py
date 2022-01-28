"""
Принимаем строку от пользователя и сделаем с ней арифметическую операцию
"""

spisok = list(input("Введите арифметическое выражение:  "))
act_list = ['+', '-', '*', '/']

for i in spisok:
    if i in act_list:
        st_num1 = ''.join(spisok[:spisok.index(i)])
        st_num2 = ''.join(spisok[spisok.index(i) + 1:])
        actn = i
try:
    srez1 = (int(st_num1) if '.' not in st_num1 else float(st_num1))
    srez2 = (int(st_num2) if '.' not in st_num2 else float(st_num2))
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
except ValueError:
    print('ошибка ввода')
