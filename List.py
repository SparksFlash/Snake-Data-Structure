letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
combined = zeros + letters
numbers = list(range(20))
chars = list("Hello World")

# print(numbers)
# print(len(chars))
print(combined)


# Accessing items
letters = ["a", "b", "c", "d"]
letters[0] = "A"
# print(letters)
# print(letters[0:3])
# print(letters[::2])
# print(numbers[::2])
# print(numbers[::-1])


# List unpacking
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# first, second, third = numbers
first, *others, last = numbers
print(first, last)
print(others)
