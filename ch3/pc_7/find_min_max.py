l = []
for i in range(0, 4):
    l.append(input(f"enter number {i+1} : "))

t = tuple(l)
print(t)

print("max : ", max(t))
print("min : ", min(t))