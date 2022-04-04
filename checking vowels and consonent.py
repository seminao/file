
#  *count vowel and consonent
f=open("shimla","r")
k=f.read().split("\n")
a=str(k)
b=list(a)
i=0
c=0
c1=0
c2=0
x=["a","e","i","o","u","A","E","I","O","U"]
while i<len(b):
    if b[i] in x:
        c=c+1
    elif b[i] in ("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","u","v","w","x","y","z"):
        c2+=1
    
    i=i+1
print("vowel:",c,"consonant:",c2)
f.close()