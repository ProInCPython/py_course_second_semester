numbers = list(map(int, input().split()))

print(len(numbers))
print(numbers[-1])
print(numbers[::-1])

if (5 in numbers) and (17 in numbers):
    print("Да")
else:
    print("Нет")

