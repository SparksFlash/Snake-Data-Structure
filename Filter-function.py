items = [
    ('product1', 10),
    ('product2', 80),
    ('product3', 40),
]


filtered = list(filter(lambda item: item[1] >= 40, items))
print(filtered)
