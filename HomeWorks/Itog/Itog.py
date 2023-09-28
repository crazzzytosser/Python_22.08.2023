import random

numbers = [random.choice([0, 1]) for _ in range(10)]  # Создаем список случайных чисел от 0 до 1

human = numbers.copy()
roboT = [1 - num for num in numbers]


print(f"{' '}{'Human':^15}{'RoboT':^10}")
print('*' * 25)

for i in range(len(human)):
    print(f'{i + 1}{human[i]:^15}{roboT[i]:^10}')
