a=input("enter username ")
b=len(a)
if(b>=10 and a.find(" ")==-1):
    print("valid username")
else:
   print("invalid username")