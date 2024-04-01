
# writing files
f = open("test.txt", 'w')
f.write("hello\nhii")
f.writelines(["\nniraj", "\nbava"])
f.close()


# reading files
f = open("test.txt", 'r')
# print(f.read())
con = f.readline()
# while(con):
#     print(con)
#     con = f.readline()

# print(f.readlines())

# for line in f:
#     print(line)


# # tell

print(f.tell())

# # seek
f.seek(0)
print(f.tell())

print(f.readline())
    
f.close()