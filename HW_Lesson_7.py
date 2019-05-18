# Сортировка пузырьком с улучшением (если соседнее число больше, то оно сразу
# "ищет" свое место в отсортированном массиве, а не просто меняется парой)

import random
nums = [random.randint(-100, 100) for _ in range(10)]
print(nums)

def sortit(my_arr):
    a = my_arr
    for i in range(len(a) - 1):
        if a[i] < a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            for j in range(i):
                if a[j] < a[i]:
                    a[j], a[i] = a[i], a[j]
    return a

print(sortit(nums))








#print(nums)
