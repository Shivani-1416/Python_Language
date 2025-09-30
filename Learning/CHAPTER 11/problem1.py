class twoD:
    def TD(self,i,j):
        self.i=i
        self.j=j
        print(f"{i}i+{j}j")



class threeD(twoD):
    def ThD(self,k):
        super().TD(5,6)
        print(f"{self.i}i+{self.j}j+{k}k")


obj=twoD()
obj.TD(5,6)
obj2=threeD()
obj2.ThD(7)