class animal:
    def __init__(self):
        print("This is a animal class\n")

class pet(animal):
    print("This is a pet class")

class wild(animal):
    print("WILD animals")


obj=wild()
obj1=pet()
