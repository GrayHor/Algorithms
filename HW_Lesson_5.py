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





