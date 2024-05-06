point = {"x": 1, "y": 2}
point = dict(x=1, y=2)    # cleaner and shorter approach

# print(point["x"])
point["x"] = 10
point["z"] = 20
print(point)

if "a" in point:
    print(point["a"])
print(point.get("a"))
