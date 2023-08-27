# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая
# проверяет счастливость билета.
#
# 385916 -> yes 123456 -> no

num = int(input("Input your number: "))
summ_left = 0
summ_right = 0
while num > 1000:
    num1 = num % 10
    summ_right += num1
    num //= 10
print(summ_right)
while num > 0:
    num2 = num % 10
    summ_left += num2
    num //= 10
print(summ_left)
all_summ = summ_left + summ_right
print(all_summ)
if summ_left == summ_right:
    print("Yes!")
else:
    print("No")
