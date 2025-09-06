import math


def calculate_circle_radius(radius):
    if radius < 0:
        return "Radius should be greater or equal to 0!"
    return math.pi * (radius ** 2)

print(calculate_circle_radius(5))
print(calculate_circle_radius(2))

def is_positive(number):
    if number == 0:
        return "return value cannot be calculated"
    return number > 0

print(is_positive(10))
print(is_positive(-10))
print(is_positive(0))
