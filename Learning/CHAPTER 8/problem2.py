def convert(n):
    return ((n/5)*9)+32


n=int(input("Enter temperacture in Celcius : "))
F=convert(n)
print(f"{n} degree Celcius is equals to {F}F")