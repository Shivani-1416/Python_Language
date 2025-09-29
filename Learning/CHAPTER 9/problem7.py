with open("python.txt","r") as f:
    lines=f.readlines()

with open("python.txt") as f:
    for i in range(1, len(lines)+1):
        n=f.readline()
        if("python" in n):
            print(i)
