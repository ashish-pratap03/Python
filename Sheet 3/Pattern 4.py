n = int(input("enter number:"))
for i in range(n+1):
    for j in range(1,1+i):
        if (j%2==0):
            print("*",end="")
        else:
            print(j,end="")
    print()
