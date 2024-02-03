# create tuple

t1 = (1,2,3)
print(t1)


# printing tuple elment
print("\n\nprinting tuple elment: \n\n")
print(t1[0])
print(t1[1])
print(t1[2])

# printing all elements of tuple
print("\n\nprinting all elements of tuple: \n\n")
for i in t1:
    print(i)
    

# delete element of tuple
print("\n\ndelete element of tuple  \n\n")
del t1

# updaing tuple
print("\n\nupdaing tuple of tuple  \n\n")
t2 = (4,5,6)
t1 = (1,2,3)
t3 = t1+t2
print(t3)

