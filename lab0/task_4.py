start, end = list(map(int, input("Введите стартовое и конечное число через пробел: ").split()))

if (start == end) and (start % 2 != 0):
    print("В этом диапазоне нет чётных чисел.")

if start % 2 != 0:
    start += 1

for i in range(start, end + 1, 2):
    print(i)
