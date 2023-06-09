# Требуется определить, можно ли от шоколадки размером 
# n × m долек отломить k долек, если разрешается сделать 
# один разлом по прямой между дольками (то есть разломить 
# шоколадку на два прямоугольника).

# Получаем размеры шоколадки от пользователя
n = int(input("Введите количество долек в шоколадке по горизонтали: "))
m = int(input("Введите количество долек в шоколадке по вертикали: "))
k = int(input("Введите количество долек, которые нужно отломить: "))

# проверяем, можно ли отломить указанное количество долек 
# (если оно меньше общего количества долек в шоколадке) 
# и есть ли прямая, по которой можно произвести разлом
if k < n*m and (k % n == 0 or k % m == 0): 
    print("Можно")
else:
    print("Нельзя")