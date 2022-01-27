"""
Функция принимает на вход три переменные. Два числа и действия над ними. В зависимости от действия выполняет операцию

"""
def arith(num1, num2, act):
    if act == '+':
        res = num1 + num2
    elif act == '-':
        res = num1 - num2
    elif act == '*':
        res = num1 * num2
    elif act == '/':
        try:
            res = num1 / num2
        except ZeroDivisionError:
            print('Деление на ноль')
            res = 0
    else:
        print('Недопустимая операция')
    return res
num1 = float(input('Введите первое число'))
num2 = float(input('Введите второе число'))
act = input('Введите действие')


print(arith(num1, num2, act))

