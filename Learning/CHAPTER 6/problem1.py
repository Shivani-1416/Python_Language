a=int(input("no 1: "))
b=int(input("no 2: "))
c=int(input("no 3: "))
d=int(input("no 4: "))

if(a>=b and a>=c and a>=d):
    print("a is greater ",a)
elif(b>=a and b>=c and b>=d):
    print("b is greater ",b)
elif(c>=a and c>=b and c>=d):
    print("c is greater ",c)
else:
    print("d is greater " , d)
