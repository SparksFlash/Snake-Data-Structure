numbers = [1, 2, 3, 4, 5]
print(*numbers)            # Unpacking operator

values = list(range(5))
values = [*range(5), *"Hello"]
print(values)
