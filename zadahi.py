def year_leap(year):  # функция проверки високосности года
    return True if year % 4 == 0 or year % 100 == 0 else False
# print(year_leap(2005))

from math import sqrt


def square(stor):  # Функция возвращает кортеж с периметром, площадью и длиной диагонали квадрата
    return stor * 4, stor ** 2, sqrt(2 * stor ** 2)
# print(square(3))

"""
Основные действия: получение элемента по ключу perem = my_dict[key1]
Добавление значения friend['hascar'] = True
Изменение значения friend['hascar'] = False
Удаление значения в словаре remove friend['nation']
оператор in     'age' in friend
Перебор словая циком for: по ключам, for key in dict.keys()
"""
def vr_goda(mon):
    seasons = {'winter': [1, 2, 12], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'fall': [9, 10, 11]}
    return [i for i in seasons.keys() if mon in seasons[i]]


print(vr_goda(5))