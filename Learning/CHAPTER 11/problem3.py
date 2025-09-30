class employee:
    name="Shivani"
    salary=100000

class salary(employee):
    def name1(self):
         print(f"{self.name} has salary {self.salary}")
    def increment(self,a):
        self.salary=self.salary+a
        print(f"{self.name} has salary {self.salary} after increment")

obj=salary()
obj.name1()
obj.increment(2000000)