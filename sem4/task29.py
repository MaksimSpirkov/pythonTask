# n = int(input())
# resoult = 0
# max_number = 1000
# while n != 0:
#  n = int(input())
#  if max_number > n:
#  resoult = n
# print(max_number)

n = int(input())
max_number = -1
while n < 0:
    n = int(input())
    if max_number < n:
        n = max_number
print(n) 