# values = []
# for x in range(5):
#     values.append(x * 2)

# In the above 3 line code is identical to -
# values = [x * 2 for x in range(5)]
values = {x: x * 2 for x in range(5)}
print(values)
