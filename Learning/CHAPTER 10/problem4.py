class calculator:
    @staticmethod
    def greet():
        print("helloooooo")
    def add(self,a,b):
        print(f"Addition",a+b)

    def multiply(self,a,b):
        print(f"Multiplication",a*b)

    def square(self,a):
        print(f"Square",a*a)
        return a*a
    def cube(self,a):
        print(f"Cube",a**3)

    def sroot(self,a):
        print(f"Square root of {a} is ",a**(1/2))

obj=calculator()
obj.greet()
a=int(input("A: "))
b=int(input("B : "))
obj.add(a,b)
obj.multiply(a,b)
s=int(input("Square : "))
sq=obj.square(s)
obj.cube(s)
obj.sroot(sq)