# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# 2 2 4

def summ(a, b):
    summ_nums = a
    count = 1
    if a < 0 and b < 0:
        return 0
    if b == 0:
        return summ_nums

    if count < b:
        a1 = a + 1
        b1 = b - 1
        count += 1
        return a1
        # elif count == b:
        #     count1 = count + b
        #     a2 = a + count1
        #     return a2

a = int(input())
b = int(input())
print(summ(a, b))
