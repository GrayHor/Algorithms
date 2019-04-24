# Смотрим разные алгоритмы сортировки
import  random
import  timeit
num = [random.randint(0, 100) for x in range(10000)]
# print(num)
# 1. Находим минимальное значение в массиве, и переносим его в другой массив c циклом
sort_num = []
def new_list_loop():
    while len(num) > 0:
        min_num = num[0]
        for i in range(len(num)):
            if min_num > num[i]:
                min_num = num[i]
        sort_num.append(min_num)
        num.remove(min_num)
#     print(sort_num)

# 2. Находим минимальное значение с помощью функции в массиве, и переносим его в другой массив
sort_num = []
def new_list_func():
    while len(num) > 0:
        min_num = min(num)
        sort_num.append(min_num)
        num.remove(min_num)
#     print(sort_num)
# new_list_func()

# 3. По каждому значению проверяем есть ли числа меньше, меняем массив и начинаем снова

def not_bubble():
    n = len(num)
    while n > 0:
        i = 0
        while i < (len(num)-1):
            if num[i] > num[i+1]:
                num[i], num[i+1] = num[i+1], num[i]
                n = len(num)
                break
            i += 1
        n -= 1
#     print(num)
# not_bubble()

# 4. Что-то похожее на пузырьковый алгоритм

def bubble():
    for i in range(len(num), -1, -1):
        while i < (len(num) - 1):
            if num[i] > num[i+1]:
                num[i], num[i+1] = num[i+1], num[i]
            i += 1
    # print(num)
# bubble()

print(timeit.timeit('new_list_loop()', setup='from __main__ import new_list_loop', number = 10000))
print(timeit.timeit('new_list_func()', setup='from __main__ import new_list_func', number = 10000))
print(timeit.timeit('not_bubble()', setup='from __main__ import not_bubble', number = 10000))
print(timeit.timeit('bubble()', setup='from __main__ import bubble', number = 10000))

# Результаты:
# Передано чисел: 100            1000                               10000

# 0.003416023000000004          0.090217813                     9.307207340000001
# 0.004228638999999999          0.005551316000000001            0.006135900000000305
# 0.004535211000000004          0.003212980999999976            0.004483892999999739
# 0.010066000000000005          0.013517722999999982            0.016997112000000314

# Вывод: алгоритм 'new_list_func()' резко увеличивает время выполнения при увеличении массива,
# хотя на небольших размерах массива показал лучший результат

