# Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. В последующих  строках 
# записаны N целых чисел Ai. Последняя строка содержит число X
    
import random, math
N = int(input('введите число элементов списка '))
my_list = []
for i in range(N):
    my_list.append(random.randint(2, 25))
print(my_list)
X = int(input('введите число для определения самого близкого элемента '))
module = abs(X-max(my_list)) # ищем разницу между введённым и максимальным
bliz_number = max(my_list) 
for i in my_list:
    if abs(X-i) < module:
        module = abs(X-i)
        bliz_number = i    
print(f'минимально близкое к числу {X} списка равно {bliz_number}')

