items = [
    ('product1', 10),
    ('product2', 80),
    ('product3', 40),
]

# prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]
print(prices)

# filtered = list(filter(lambda item: item[1] >= 40, items))
filtered = [item for item in items if item[1] >= 40]
print(filtered)
