items = [
    ('product1', 10),
    ('product2', 80),
    ('product3', 40),
]


x = list(filter(lambda item: item[1] >= 10, items))
print(x)
