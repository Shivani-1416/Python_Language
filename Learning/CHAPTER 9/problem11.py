with open("this.txt","r") as f:
    data=f.read()
with open("renamed_by_python.txt","w") as f:
    f.write(data)

print()