def pattern(n):
    for i in range(1,n+1):
        print("*"*(n+1-i),end="")
        print(" "*(i+1))


n=int(input("Enter value of N: "))
pattern(n)