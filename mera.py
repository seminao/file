delhi=open("delhi.txt","a")
shimla=open("shimla","a")
jaipur=open("jaiput.txt","a")
others=open("others.txt","a")
f=open("filequestion.txt","r")
a=f.read()
b=a.split("\n")
i=0
while i<len(b):
    if "delhi" in b[i]:
        delhi.write(b[i])
        delhi.write("\n")
    elif "shimla" in b[i]:
        shimla.write(b[i])
        shimla.write("\n")
    elif "jaipur" in b[i]:
        jaipur.write(b[i])
        jaipur.write("\n")
    else:
        others.write(b[i])
        others.write("\n")
    i=i+1
f.close()