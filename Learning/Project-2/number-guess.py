import random

class game:
    @staticmethod
    def greet():
        print("\n\n\t\t\t\t-------S T A R T-----")
        print("""
        📘 Rule Book
            1. Guess the number.
            2. I’ll tell you if your guess is too high or too low.
            3. Keep guessing until you get it right.
            4. I’ll show you how many tries you took.

        Good luck! 🎯
        """)

    def number(self):
        list1 = []
        for i in range(0, 101):
            list1.append(i)

        num = random.choice(list1)
        return num

    def choose(self, num, ch, i):
        self.num = num
        self.ch = ch
       
        if (ch == num):
            print("\n" + "\t" * i + "-"*11+"Congratulationssss !!"+"-"*11)
            return True 
        elif (ch > num):
            print("\n" + "\t" * i + "Enter small number")
        elif (ch < num):
            print("\n" + "\t" * i + "Enter greater number")
        else:
            print("\n" + "\t" * i + "Invalid number")

    def imp(self):
        b=0
        for i in range(0, 3):
            ch = int(input("\n\n" + "\t" * i + "Enter your number : "))
            b=b+1
            a = obj.choose(num, ch, i)
        
            if (a):
                print("\n\n" + "\t" * i +"You Wonnn !!!")
                break
            if(b==3):
                print("\n\n"+"\t"*i+"_."*15+"B E T T E R  L U C K  N E X T  T I M E"+"_."*15+"\n\n")
        

class easy(game):
     def number(self):
        return 5

class medium(game):
     def number(self):
        list1 = []
        for i in range(0, 51):
            list1.append(i)

        num = random.choice(list1)
        return num
    
a=1
while(a==1):
    print("\n\n\t\t\t\t-------W E L C O M E-----\n\n\n")
    choice=int(input("""\t\t\t\t--Please select level--
                        1. EASY (GUESS NUMBER BETWEEN 0 to 10)
                        2. MODERATE (GUESS NUMBER BETWEEN 0 to 50)
                        3. HARD (GUESS NUMBER BETWEEN 0 to 100)\n"""))

    if (choice==1):
        obj = easy()
        obj.greet()
        num = obj.number()
        obj.imp()
    elif(choice==2):
        obj = medium()
        obj.greet()
        num = obj.number()
        obj.imp()
    elif(choice==3):
        obj = game()
        obj.greet()
        num = obj.number()
        obj.imp()


    print("\n\n"+"\t"*3+"_."*15+" R E S U L T"+"_."*15+"\n\n")

    print("\n\n"+"\t"*3+"Number chosen by you :- "+str(obj.ch))
    print("\n"+"\t"*3+"Number chosen by Computer :- "+str(num)+"\n")
    

    a=int(input("""
            Press : 1. Replay
                    2. ESC
    """))
    if a==2:
        print("\t\t\tT H A N K  Y O U\t\t\t")

