import random
def computer(a): 
        U1=input("\n\tEnter your choice :\n\tStone\n\tPaper\n\tScissor\n\tYour Input : ")
        if(U1.lower()==a):
            print(f"\n\t-----Draw-----\n\n\tYOU : {U1}  computer : {a}")
            return "draw"
        elif(U1.lower()=="stone" and a=="paper" ):
            print(f"\n\t-----COMPUTER WON-----\n\n\tYOU : {U1}  computer : {a}")
            return "a"
        elif(U1.lower()=="stone" and a=="scissor"):
            print(f"\n\t-----YOU WON-----\n\n\tYOU : {U1}  computer : {a}")
            return "U1"
        elif(U1.lower()=="paper" and a=="stone"):
            print(f"\n\t-----YOU WON-----\n\n\tYOU : {U1}  computer : {a}" )
            return "U1"
        elif(U1.lower()=="paper" and a=="scissor"):
            print(f"\n\t-----COMPUTER WON-----\n\n\tYOU : {U1}  computer : {a}")
            return "a"
        elif(U1.lower()=="scissor" and a=="stone"):
            print(f"\n\tCOMPUTER WON-----\n\n\tYOU : {U1}  computer : {a}")
            return "a"
        elif(U1.lower()=="scissor" and a=="paper"):
            print(f"\n\t-----YOU WON-----\n\n\tYOU : {U1}  computer : {a}")
            return "U1"
        else:
            print("--------I N V A L I D  C H O I C E--------")
   


def USER():
        u1=input("\n\tUser 1\n\tEnter your choice :\n\tStone\n\tPaper\n\tScissor\n\tYour Input : ")
        u2=input("\n\tUser 2\n\tEnter your choice :\n\tStone\n\tPaper\n\tScissor\n\tYour Input : ")

        if(u1.lower()==u2.lower()):
            print("\n\t-----Draw-----\n")
            return "draw"
        elif(u1.lower()=="stone" and u2.lower()=="paper" ):
            print("\n\t-----User 2 WON-----\n")
            return "U2"
        elif(u1.lower()=="stone" and u2.lower()=="scissor"):
            print("\n\t-----User 1 WON-----\n")
            return "U1"
        elif(u1.lower()=="paper" and u2.lower()=="stone"):
            print("\n\tUser 1 WON-----\n" )
            return "U1"
        elif(u1.lower()=="paper" and u2.lower()=="scissor"):
            print("\n\t-----User 2 WON-----\n")
            return "U2"
        elif(u1.lower()=="scissor" and u2.lower()=="stone"):
            print("\n\tUser 2 WON-----\n")
            return "U2"
        elif(u1.lower()=="scissor" and u2.lower()=="paper"):
            print("\n\t-----User 1 WON-----\n")
            return "U1"
        else:
            print("--------I N V A L I D  C H O I C E--------")
def code():
    print("\n                   ........W E L C O M E...........\n")
    user=input("You want to play with ?\n1. Computer (type computer)\n2. User 2 (type user)\nYour Choice : ")

    if(user.lower()=="computer"):
        choice=int(input("\nHOW MANY TIMES YOU WANT TO PLAY ?\n(ENTER NUMBER): "))
        score=0
        d=0
        c=0
        for i in range(1,choice+1):
            l1=["stone","paper","scissor"]
            a=random.choice(l1)
            win=computer(a)
            if(win=="U1"):
                score=score+1
                print(f"\n\tCurrent Score=>  YOU : {score} || COMPUTER : {c} || DRAW : {d}\n")
            elif(win=="draw"):
                d=d+1
                print(f"\n\tCurrent Score=>  YOU : {score} || COMPUTER : {c} || DRAW : {d}\n")
            elif(win=="a"):
                c=c+1
                print(f"\n\tCurrent Score=>  YOU : {score} || COMPUTER : {c} || DRAW : {d}\n")
        print(f"\n\t\t\tFinal Score :\n ")
        if(score>=1/choice):
            print(f"\t\t\tUSER SCORE : {score}\n\t\t\tCOMPUTER SCORE : {c}\n\t\t\tDRAW : {d}\n\n\t\t\t    ====R E S U L T====  \n\n\t\t\t---USER WON BY {score} SCORE---")
        elif(c>=1/choice):
            print(f"\t\t\tUSER SCORE : {score}\n\t\t\tCOMPUTER SCORE : {c}\n\t\t\tDRAW : {d}\n\n\t\t\t    ====R E S U L T====  \n\n\t\t\t---COMPUTER WON BY {c} SCORE---")
        else:
            print(f"\t\t\tUSER SCORE : {score}\n\t\t\tCOMPUTER SCORE : {c}\n\t\t\tDRAW : {d}\n\n\t\t\t    ====R E S U L T====  \n\n\t\t\t---FINAL DRAW---")

    elif(user.lower()=="user"):
        choice=int(input("\nHOW MANY TIMES YOU WANT TO PLAY ?\n(ENTER NUMBER): "))
        d=0
        U2=0
        U1=0
        for i in range(1,choice+1):
            win=USER()
            if(win=="draw"):
                d=d+1
                print(f"\n\tCurrent Score=> USER 1 : {U1} || USER 2 : {U2} || DRAW : {d}\n")
            elif(win=="U2"):
                U2=U2+1
                print(f"\n\tCurrent Score=> USER 1 : {U1} || USER 2 : {U2} || DRAW : {d}\n")
            elif(win=="U1"):
                U1=U1+1
                print(f"\n\tCurrent Score=> USER 1 : {U1} || USER 2 : {U2} || DRAW : {d}\n")
        print(f"\n\t\t\tFinal Score :\n ")
        if(U1>=1/choice):
            print(f"\t\t\tUSER 1 SCORE : {U1}\n\t\t\tUSER 2 SCORE : {U2}\n\t\t\tDRAW : {d}\n\n\t\t\t    ====R E S U L T===  \n\n\t\t\t---USER 1 WON BY SCORE {U1}---")
        elif(U2>=1/choice):
            print(f"\t\t\tUSER 1 SCORE : {U1}\n\t\t\tUSER 2 SCORE : {U2}\n\t\t\tDRAW : {d}\n\n\t\t\t    ====R E S U L T====  \n\n\t\t\t---USER 2 WON BY SCORE {U2}---")
        elif(d>=1/choice):
            print(f"\t\t\tUSER 1 SCORE : {U1}\n\t\t\tUSER 2 SCORE : {U2}\n\t\t\tDRAW : {d}\n\n\t\t\t    ====R E S U L T====  \n\n\t\t\t---HERE IS A FINAL DRAW---")
        
    else:
          print("\n--------I N V A L I D  C H O I C E--------\n")
          
num=0
while(num>=0):
    begin=input(("Shall we start ?\nEnter Y/N: "))
    if(begin.lower()=='y'):
        code()
    elif(begin.lower()=='n'):
        print("\n\n--------Thank you--------")    
        break
    else:
        print("\n--------I N V A L I D  C H O I C E--------")

    c2=input("You want to play again ?\nEnter (Y/N): ")
    if(c2.lower()=="y"):
        num=num+1
        code()
    elif(c2.lower()=='n'):
         num=num-1
         print("--------Thank you--------")
         break
    else:
        print("\n--------I N V A L I D  C H O I C E--------")
