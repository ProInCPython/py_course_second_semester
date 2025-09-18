import numpy as np

a = np.random.randint(1, 11, (5,5))
b = np.random.randint(1, 11, (5,5))
print("Матрица A:\n", a)
print("Матрица B:\n", b)
print("Поэлементное произведение:\n", np.multiply(a, b))
print("Матричное произведение:\n", np.dot(a,b))
print("Определитель матрицы A:\n", np.linalg.det(a))
print("Транспонированная матрица B:\n", b.T)
if np.linalg.det(a) != 0:
    print("Обратная матрица для A:\n", np.linalg.inv(a))
    c = np.sum(a, axis=1).reshape(-1, 1)
    a_inv = np.linalg.inv(a)
    print(np.dot(a_inv, c))
else:
    print("Обратной матрицы не существует!")


