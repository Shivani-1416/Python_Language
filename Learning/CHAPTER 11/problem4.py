class complex:
    def num(self,i,j):
        self.i=i
        self.j=j
        print(f"{self.i}i+{self.j}j")
        return i,j

    def add(self,r,r2,i,i2):
        self.r=r
        self.r2=r2
        self.i=i
        self.i2=i2
        print(f"Addition : {r+r2}i+{i+i2}j")

    def mul(self,r,r2,i,i2):
        self.r=r
        self.r2=r2
        self.i=i
        self.i2=i2
        a=r*i2
        b=i*r2
        print(f"product : {r*r2}i^2+{a}ij+{b}ji+{i*i2}j^2")


obj1=complex()
r,i=obj1.num(5,6)
r2,i2=obj1.num(3,4)
obj1.add(r,r2,i,i2)
obj1.mul(r,r2,i,i2)