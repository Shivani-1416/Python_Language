with open("this.txt","r") as f:
    data=f.read()

with open("copy.txt","r") as f:
    data1=f.read()

if data==data1:
    print("Content is identical")
else:
    print("data is not identical")

