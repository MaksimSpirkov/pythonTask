# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

def print_powers_of_two():
    N = int(input("Введите число N: ")) # Ввод числа N с клавиатуры и преобразование его в целое число
    k = 0                               # Инициализация переменной k, которая будет служить показателем степени
    power_of_two = 1                    # Инициализация переменной power_of_two, начинаем с 2^0 = 1
    while power_of_two <= N:            # Пока значение степени не превосходит N
        print(power_of_two)             # Выводим текущее значение степени двойки
        k += 1                          # Увеличиваем значение k на 1, чтобы перейти к следующей степени
        power_of_two = 2 ** k           # Вычисляем новое значение степени двойки, умножая 2 на текущее значение k

# Вызов функции
print_powers_of_two()