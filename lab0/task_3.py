a, b, c = list(map(int, input("Введите 3 числа через пробел: ").split()))



if a <= b:
    if a <= c:
        print(a)
    else:
        print(c)
else:
    if b <= c:
        print(b)
    else:
        print(c)