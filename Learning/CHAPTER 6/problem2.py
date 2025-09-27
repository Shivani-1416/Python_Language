print("Enter Marks of each subject out of 100")
a=int(input("Marks of DS : "))
b=int(input("Marks of TOC : "))
c=int(input("Marks of Python : "))


if(a<33):
    print("Failed in DS")
elif(b<33):
    print("Failed in TOC")
elif(c<33):
     print("Failed in python")
else:
    print("passed in each subject")

total=a+b+c

if(a<33 or b<33 or c<33 ):
    print("overall failed")
elif(total<120):
    print("overall failed")
else:
    print("OVERALL PASSED ")

   
