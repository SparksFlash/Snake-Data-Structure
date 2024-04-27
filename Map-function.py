items = [
    ('product1', 10),
    ('product2', 80),
    ('product3', 40),
]

# prices = []
# for item in items:
#     prices.append(item[1])
# print(prices)

# we can also achieve in this way
x = map(lambda item: item[1], items)
for item in x:
    print(item)

# we can also achieve in this way also
prices = list(map(lambda item: item[1], items))
print(prices)
