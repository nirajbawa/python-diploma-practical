l1 = [1,2,3,4,5]

# nappend
print("\n\nappend : \n\n")
l1.append(3)
print(l1)


# extend
print("\n\nextend : \n\n")
l1.extend(["niraj", "bava"])
print(l1)


# sort
print("\n\nsort : \n\n")
l2 = [3,1,2]
l2.sort() #only working with same data types
print(l2)


# count
print("\n\ncount : \n\n")
print(l1.count(2))


# copy
print("\n\ncopy : \n\n")
lc = l1.copy()
print(l2)

# index
print("\n\nindex : \n\n")
print(l1.index(5))

# insert
print("\n\ninsert : \n\n")
l1.insert(8,20)
print(l1)


# reverse
print("\n\nreverse : \n\n")
l1.reverse()
print(l1)
