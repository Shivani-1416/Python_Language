with open("poem.txt") as f:
    data=f.read()
    if("twinkle" in data.lower()):
        print("Twinkle is presentt in a given file")
    else:
        print("Twinkle is not in a file")