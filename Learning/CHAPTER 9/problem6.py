with open("log.txt","r") as f:
    data=f.read()

if("python" in data.lower()):
    print("\nPython is present")
else:
    print("Absent")