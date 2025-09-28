l=["Shivani","suhani","Sarthak","Nikita"]

for i in range(len(l)):
    if(l[i].startswith("S") or l[i].startswith("s")):
        print(f"HEllo {l[i]}")
    else:
        print(f"Bye {l[i]}")