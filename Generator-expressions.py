# Here we use parantheses for creating generator object
from sys import getsizeof
values = (x * 2 for x in range(10))
print(values)
for x in values:
    print(x)


test = (x * 2 for x in range(1000))
print("Gen :", getsizeof(test))
