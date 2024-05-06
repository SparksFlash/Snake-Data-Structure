point = {"x": 1, "y": 2}
point = dict(x=1, y=2)    # cleaner and shorter approach

# print(point["x"])
point["x"] = 10
point["z"] = 20
print(point)

if "a" in point:
    print(point["a"])
print(point.get("a", 0))
del point["x"]
print(point)

# How to loop over dictionaries
for key in point:
    print(key, point[key])

# another way to iterate and get the velue with tuple

for x in point.items():
    print(x)
