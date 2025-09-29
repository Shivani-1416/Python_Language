class railway:
    def __init__(self):
        print("-----Hellooooooo-----")
    @staticmethod
    def greet():
        print("---I N D I A N  R A I L W A Y S---")


    def trains(self):
        print("1 Rajdhani express")
        print("2 Vande Bharat")
    
    def tickets(self):
        a=100
        print(f"Available seats are {a}")
        n=int(input("Enter number of tickets to book : "))
        print(f"{n} Tickets booked\nAvailable tickets {a-n}")

    def rajdhani(self):
        self.greet()

        print("\nW E L C O M E  T O  R A J D H A N I  E X P R E S S")
        self.tickets()

    def vandebharat(self):
        self.greet()
        
        print("\nW E L C O M E  T O  V A N D E  B H A R A T")
        self.tickets()


print("\n")
obj=railway()
obj.trains()
print("\n")
# obj.tickets()
a=int(input("choose train : "))
print("\n")
if(a==1):
    obj.rajdhani()
elif(a==2):
    obj.vandebharat()
else:
    print("-----I N V A L I D  C H O I C E-----")