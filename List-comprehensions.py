items = [
    ('product1', 10),
    ('product2', 80),
    ('product3', 40),
]

# prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]
print(prices)
