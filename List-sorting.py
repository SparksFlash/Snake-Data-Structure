numbers = [3, 51, 8, 6, 4, 10]
# numbers.sort()
# print(numbers)

# numbers.sort(reverse=True)
print(sorted(numbers, reverse=True))
print(numbers)


items = [
    ('product1', 10),
    ('product2', 80),
    ('product3', 40),
]


# def sort_item(item):
#     return item[1]


# items.sort(key=sort_item)
# print(items)


# Sorting without func using lamda
items.sort(key=lambda item: item[1])
print(items)
