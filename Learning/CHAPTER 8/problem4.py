def SUM(n):
    if(n==1):
        return 1
    else:
        return n+SUM(n-1)




n=int(input("Enter value of N: "))
sum1=SUM(n)
print(f"SUM OF FIRST {n} NATURAL NUMBER IS {sum1}")