def fact(n):
   if(n==1 or n==0):
        return 1
   else:
       return n*fact



n=int(input("Enter number : "))
factorial=fact(n)
print(f"Factorial is {factorial}")

