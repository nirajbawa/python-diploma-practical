# create set

s = {1,2,3}


# acessing set
print("\n\nacessing set :\n\n")
for i in s:
    print(i)
    
    
# updating set
print("\n\nupdating set :\n\n")
s.add("niraj")
s.update({4, 5, 6})
print(s)

# deleting set elements
print("\n\ndeleting set elements :\n\n")
s.remove("niraj")
print(s)
s.discard(1)
print(s)
print(s.pop())
del s
