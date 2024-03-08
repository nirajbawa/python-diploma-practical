# union
print("\n\nunion : \n\n")
s1 = {1,2,3}
s2 = {3,4,1}
s3 = s1 | s2
print(s3)

# intersection
print("\n\nintersection : \n\n")
s3 = s1 & s2
print(s3)

# difference
print("\n\ndifference : \n\n")
s3 = s1-s2
print(s3)
s3 = s2-s1
print(s3)

# symmetric difference update
print("\n\nsymmetric difference update : \n\n")
s3 = s1 ^ s2
print(s3)