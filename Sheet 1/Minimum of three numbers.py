a = int(input("Enter number a: "))
b = int(input("Enter number b: "))
c = int(input("Enter number c: "))

if a <= b and a <= c:
    print("Min:", a)
elif b <= a and b <= c:
    print("Min:", b)
else:
    print("Min:", c)
