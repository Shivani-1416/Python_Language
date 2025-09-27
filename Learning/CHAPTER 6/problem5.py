list1=["Shivani","Gaurav","Suhani","Gayatri"]
enter=input("Enter a name :")
name=enter.capitalize()

if(list1[0]==name or list1[1]==name or list1[2]==name or list1[3]==name):
    print(f"{name} Already present in list")
    print(list1)
else:
    print(f"{name} is not present in list ")
    list1.append(name)
    print(list1)