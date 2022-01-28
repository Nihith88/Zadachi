"""
Принимаем строку от пользователя и сделаем с ней арифметическую операцию
"""

spisok = list(input("Введите арифметическое выражение:  "))  # Запрос строки у пользователя
act_list = ['+', '-', '*', '/']  # Список операций арифметики

border = (lambda i: spisok.index(i) for i in spisok if i in act_list)
actn = (i for i in spisok if i in act_list)
print(border, type(border))
print(actn, type(actn))
"""st_num1 = ''.join(spisok[:border])
st_num2 = ''.join(spisok[border + 1:])
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
    print('ошибка ввода')"""
