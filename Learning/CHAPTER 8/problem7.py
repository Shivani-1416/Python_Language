def word(name,rem):
    name.remove(rem)
    return name



name=["Yashi","Shivani","Prachi","Gayatri"]
rem=input("Enter word to remove : ")
name=word(name,rem)
print(f"removed word is {rem} {name}")