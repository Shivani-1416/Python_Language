a="Make a lot of money"
b="buy now"
c="subscribe this"
d="click this"


msg=input("Enter a comment :")
if(msg.find(a)==-1 or msg.find(b)==-1 or msg.find(c)==-1 or msg.find(d)==-1):
    print("SPAM COMMENT")
else:
    print("NOT SPAM")