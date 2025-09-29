class Employee:
    name="NULL"
    salary=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        print(self.name+" "+str(self.salary))


name=input("name : ")
salary=input("salary : ")
obj=Employee(name,salary)