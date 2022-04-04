def my():
    f=open("name.txt","r")
    d=f.readlines()
    i=0
    c=0
    while i<len(d):
        if d[i][0]=="l":
            c=c+1
            # f.write(c)
        i=i+1
    print(c)
    f.close ()
my()