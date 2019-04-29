# Пример 1
# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

from pympler import asizeof

# a = (input('Введите числа: ')).split()
# b = []
# for i in range(len(a)):
#     if int(a[i]) % 2 == 0:
#         b.append(i)
# print(*b)
# print(asizeof.asizeof(a))
# print(asizeof.asizeof(b))

# в зависимости от количества переданных в массив данных изменяется и размер занимаемой памяти




import collections

n = (input('Введите количество предприятий: '))
factory = collections.namedtuple('factory', ['name', 'year_profit'])
factories = []

for i in range(int(n)):
    fname = input('Название предприятия: ')
    a = input('Прибыль за первый квартал: ')
    b = input('Прибыль за второй квартал: ')
    c = input('Прибыль за третий квартал: ')
    d = input('Прибыль за четвертый квартал: ')
    year_profit = int(a) + int(b) + int(c) + int(d)
    ffactory = factory(name=fname, year_profit=year_profit)
    factories.append(ffactory)


summ = 0
for i in range(int(n)):
    summ += factories[i][1]
average_profit = summ / int(n)


print('Средняя прибыль: ', average_profit)

print('Предприятия с прибылью выше среднего: ')
for i in range(int(n)):
    if factories[i][1] > average_profit:
        print('Название: ', factories[i][0], 'прибыль: ', factories[i][1])

print('Предприятия с прибылью ниже среднего: ')
for i in range(int(n)):
    if factories[i][1] < average_profit:
        print('Название: ', factories[i][0], 'прибыль: ', factories[i][1])

print(asizeof.asizeof(factories))
print(asizeof.asizeof(average_profit))
#
# При увеличении кол-ва предприятий кортеж увеличивается, а память, занимаемая  средним значением, практически нет