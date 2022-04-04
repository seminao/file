# *removing words after fullstop(.)
f=open("on","r")
d=f.read()
a=list(d)
i=0
while i<len(a):
    print(a[i],end="")
    i+=1
    if a[i]==".":
        break
f.close()
# **
user=str(input("enter file name:"))
a=list(user)
i=0
while i<len(a):
    print(a[i],end="")
    i+=1
    if a[i]==".":
        break
