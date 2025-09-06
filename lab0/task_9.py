import random

lst = [random.randint(-10, 10) for i in range(15)]

first = list(filter(lambda a : a > 0, lst))
second = [i ** 2 for i in lst]
print(first)
print(second)

