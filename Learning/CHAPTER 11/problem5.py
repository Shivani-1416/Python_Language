class vector:
    def num(self,i,j):
        self.i=i
        self.j=j
        print(f"{self.i}i+{self.j}j")
        return i,j

    def add(self,i,j,i2,j2):
        self.i=i
        self.j=j
        self.i2=i2
        self.j2=j2
        a=i+i2
        b=j+j2
        print(f"Addition : {a}i+{b}j")

#(5i+6j).(3i+4j)=(5.3)+(6.4)
    def mul(self,i,j,i2,j2):
        self.i=i
        self.j=j
        self.i2=i2
        self.j2=j2
        a=i*i2
        d=j*j2
        print(f"product : {a}+{d}={a+d}")


obj1=vector()
i,j=obj1.num(5,6)
i2,j2=obj1.num(3,4)
obj1.add(i,j,i2,j2)
obj1.mul(i,j,i2,j2)