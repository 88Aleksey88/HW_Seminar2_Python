# Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

n = int(input("Введите число: "))
list = []
i = 2
while i <= n:
    list.append(i)
    i = i * 2
print (list)