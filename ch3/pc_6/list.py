
# create list 

l = ["niraj", "umesh", "bava"]
print(l)

# access list element
print("\n\naccessing list elements : \n\n")
print(l[0])
print(l[1])
print(l[2])

# printing list elements

print("\n\nprinting all list elements : \n\n")
for i in l:
    print(i)
    
    
# printing list elements
print("\n\nprinting all list elements : \n\n")
for i in enumerate(l):
    print(i)
    
# printing list elements
print("\n\nprinting all list elements : \n\n")                                                                                                           
for i in l:
    print(i)
    
# deleting elements of list
print("\n\ndeleting elements of list : \n\n")
print(l.pop(1))
print(l.pop())

# remove list elements
print("\n\nremove list elements : \n", l)
l.remove("niraj")
print(l)


# updating list 
print("\nupdating list\n")
l.append("realme")
l.append("apple")
l.append("samsung")
l[2] = "oppo"
del l[0]
print(l)
