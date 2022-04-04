f=open("name.txt","w")
user=int(input("enter the number"))
i=0
while i<=user:
    n=input("enter the name")
    f.write(n+"\n")
    i=i+1
f.close()
