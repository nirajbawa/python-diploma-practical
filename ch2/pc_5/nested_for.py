end = int(input("enter number : "))

for i in range(0, end):
    for j in range(0, i):
        print("*", end="")
    print()
    