with open("word.txt","r") as f:
    data=f.read()

#print(data)
    
content=(data.lower()).replace("donkey","#####")
#print(content)
with open("word.txt","w+") as f:
     f.write(content)
     print("Updated")
        
with open("word.txt","r") as f:
    data1=f.read()
    print(data1)


    