items = [
    ('product1', 10),
    ('product2', 80),
    ('product3', 40),
]

# prices = []
# for item in items:
#     prices.append(item[1])

# print(prices)

x = map(lambda item: item[1], items)
for item in x:
    print(item)
