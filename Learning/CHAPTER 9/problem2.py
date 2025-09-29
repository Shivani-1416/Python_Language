with open("Hi-score.txt","r") as f:
    data=f.read()
   
n=int(input("Enter data : "))
if(n>int(data)):
    with open("Hi-score.txt","w+") as f:
        f.write(str(n))
   

