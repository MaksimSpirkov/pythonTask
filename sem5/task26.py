# Задача 26:  Напишите программу, которая на вход 
# принимает два числа A и B, и возводит число А 
# в целую степень B с помощью рекурсии.

import os
os.system('cls')


def power(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * power(a, b-1)

a = int(input("Введите число: "))
b = int(input("Введите степень: "))

result = power(a, b)

print(f"{a} в {b} степени будет {result}")