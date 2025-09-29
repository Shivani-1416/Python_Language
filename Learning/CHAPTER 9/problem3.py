for i in range(2,6):
    with open(f"problem3\\{i}.txt","w") as f:
        for j in range(1,11):
            a=i*j
            f.write(f"{i} * {j} = "+str(a)+"\n")

print("Successfull")

    