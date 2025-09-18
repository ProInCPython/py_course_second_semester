import math

def safe_apply(func, data):
    results = []
    errors = []
    for i in data:
        try:
            results.append(func(i))
        except Exception as err:
            errors.append((i, err.__class__.__name__))

    return results, errors

print(safe_apply(lambda x : math.sqrt(x), [4, 16, 'text', -25, 9.0]))