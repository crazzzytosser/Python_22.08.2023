# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B
# с помощью рекурсии. \
#     A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8


def step(a, b):
    mult = 1
    count = 0
    if a <= 0:
        return 0
    while b != count:
        a1 = a * a
        mult *= a
        count += 1
    return mult


a = int(input("Input a: "))
b = int(input("Input b: "))
print(step(a, b))
