list1=["shivani","modern","iit","and"]

with open("fifth.txt") as f:
    data=f.read()
print(data+"\n")
for i in list1:    
    data=data.replace(i,"***")


with open("fifth.txt","w") as f:
    f.write(data)

print(data)

   