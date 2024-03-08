s1 = {1,2,3}

s2 = s1.copy()
print(s2)

print(s1.isdisjoint(s2))

print(s1.issubset(s2))

print(s1.issuperset(s2))

s1.intersection_update(s2)
print(s1)

s1.symmetric_difference_update(s2)
print(s1)
