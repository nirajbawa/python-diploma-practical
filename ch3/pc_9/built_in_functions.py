d = {"name":"niraj", "class":"ty-co"}
print(d.get("name"))

print(d.keys())

print(d.values())

print(d.items())

d2 = d.copy()
print(d2)

d.clear()
print(d)

l = ["name", "class"]
val = 3

d3 = dict.fromkeys(l, val)
print(d3)