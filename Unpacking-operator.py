numbers = [1, 2, 3, 4, 5]
print(*numbers)

# Unpacking operator
# Using this operator we can combined multiple list

values = list(range(5))
values = [*range(5), *"Hello"]
print(values)

first = [1, 2, 3, 4]
second = [7, 8, 9]
result = [*first, "a", *second, *"Hello"]
print(result)

one = {"x": 1}
two = {"y": 2, "z": 1}
combined = {**one, **two, "z": 9}
print(combined)
