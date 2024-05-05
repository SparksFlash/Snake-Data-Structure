numbers = [1, 1, 2, 3, 4, 5]
uniques = set(numbers)
print(uniques)

second = {1, 7, 8, 6}

# Union and Intersection
print(uniques | second)
print(uniques & second)
print(uniques - second)
print(uniques ^ second)
