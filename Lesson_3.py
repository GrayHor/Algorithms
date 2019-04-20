# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
print({n: (len([x for x in range(2, 100)]) // n) for n in range(2,10)})

# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

a = (input('Введите числа: ')).split()
b = []
for i in range(len(a)):
    if int(a[i]) % 2 == 0:
        b.append(i)
print(*b)

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
a = (input('Введите числа: ')).split()
min_a = a.index(min(a))
max_a = a.index(max(a))
a[min_a], a[max_a] = a[max_a], a[min_a]

print(a)

# 4. Определить, какое число в массиве встречается чаще всего.
import random
num = [random.randint(1, 9) for x in range(20)]
max = 0
for i in range(len(num)):
    if num.count(num[i]) > max:
        max = num.count(num[i])
        ans = num[i]
print(num)
print('Число', ans, 'встречается', max, 'раз(а)')

# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
import random
num = [random.randint(-100, -1) for x in range(20)]
min_num = 0
for i in range(len(num)):
    if num[i] < min_num:
        min_num = num[i]
        ind = i
print(num)
print('Максимальный отрицательный элемент:', min_num, 'его индекс:', ind)

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
import random
num = list(set([random.randint(1, 100) for x in range(20)]))
max_el = num[0]
max_ind = 0
min_el = num[0]
min_ind = 0
summ = 0

for i in range(len(num)):
    if num[i] > max_el:
        max_el = num[i]
        max_ind = i
    elif num[i] < min_el:
        min_el = num[i]
        min_ind = i
if min_ind > max_ind:
    min_ind, max_ind = max_ind, min_ind
for i in range(min_ind + 1, max_ind):
    summ += num[i]

print(summ)
