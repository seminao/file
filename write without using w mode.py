# *
f=open("creat without w","a+")
user=int(input("enter the number"))
i=0
while i<=user:
    user2=input("enter the name")
    f.writelines(user2+"\n")
    i=i+1
f.close()
