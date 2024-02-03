# concatenation using +

print("\n\nconcatenation using + : \n\n")
l1 = [1,2,3,4]
l2 = [5,6,7,8]
l3 = l1+l2
print(l3)


# repeatation using *
print("\n\nrepeatation using * : \n\n")
l4 = l3*2
print(l4)

# finding length of a list
print("\n\nfinding length of a list : \n\n")
print(len(l4))


# membership
print("\n\nmembership : \n\n")

print(5 in l4)
print(5 not in l4)

# list slice
print("\n\list slice : \n\n")
print(l4[0:5]) #this function works s to n-1
