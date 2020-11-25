"""
    1. Создать функцию, которая выводит на экран цифру, введенную пользоватлем в консоли.

    2. Написать программу, которая принимает 5 значений, введенных пользователем из консоли, сохранит их в список,
    затем передаст значения в фукцию, которая выводит на экран сумму значений списка.

    3. Написать программу, которая:
    - выводит следующее меню на экран
        1. Ввести значения а и b
        2. Умножить значения а и b
        3. Делить а на b
        4. Выход
    - реализует каждую опцию как фукцию
    - реализует все ошибки и исключения.
"""




#  1
def function (value):
    return value

print('Введите значение: ')
a = int(input())
print(function(a))


#  2

def function2(array):
    total = 0
    for element in range(len(array)):
        total += array[element]

    return total

d = []
count, i = 0, 0
while i < 5:
    n = int(input('Введите число'))
    i += 1
    d.append(n)


print(function2(d))

# 3
def user_input():
    A = int(input('a: '))
    B = int(input('b: '))

    return A, B


def multiplication(A, B):
    return A * B


def divider(A, B):
    return A / B


def quit_pr():
    return True


a = 0
b = 0

while True:

    print('''1. Ввести значения а и b
2. Умножить значения а и b
3. Делить а на b
4. Выход''')

    try:
        user_choice = int(input('>>> '))

        if user_choice != 4:
            if user_choice == 1:
                a, b = user_input()
                print(f'a: {a}, b: {b}')
            elif user_choice == 2:
                print(f'a * b = {multiplication(a, b)}')
            elif user_choice == 3:
                print(f'a / b = {divider(a, b)}')
            else:
                raise ValueError
        else:
            if quit_pr() is True:
                print('Выход из программы...')
                break
    except (ValueError, ZeroDivisionError):
        print('Допущена ошибка.')
