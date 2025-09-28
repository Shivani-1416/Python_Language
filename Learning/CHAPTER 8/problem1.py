def greatest(a,b,c):
    if(a>=b and a>=c ):
        print(a)
    elif(b>=a and b>=c):
        print(b)
    else:
        print(c)

a=int(input("Enter A : "))
b=int(input("Enter B : "))
c=int(input("Enter C : "))
greatest(a,b,c)
print("Thank you")