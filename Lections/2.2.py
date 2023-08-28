# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи
# оно является, то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.
#
# Input:     5
#
# Output:  6

a = 5
fib1 = 0
fib2 = 1
n = 2
while fib2 < a:
    n = n + 1
    # fib1, fib2 = fib2, fib1 + fib2
    temp = fib2
    fib2 = fib1 + fib2
    fib1 = temp
if fib2 == a:
    print(n)
else:
    print(-1)