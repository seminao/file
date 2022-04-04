# def file_read(fname):
#     txt=open(fname)
#     print(txt.read())
# file_read("shimla")

# def file_read(fname,nlines):
#     from itertools import islice
#     with open(fname)as f:
#         for line in islice(f,nlines):
#             print(line)
# file_read("shimla",2)

# def my():
#     file=open("shimla")
#     num=int(input("enter number:"))
#     i=0
#     while i<num:
#         print(file.readline())
#         i+=1
# my()

# def file(fname):
#     c=[]
#     f=open(fname)
#     for i in f:
#         c.append(i)
#     print(c)
# file("shimla")

# f=open("shimla","r")
# a=[]
# for i in f:
#     a.append(i)




# user=input("enter file name")
# f=open(user,"r")
# u=f.read().split()
# print(u)
# i=0
# max=u[i]
# while i<len(u):
#     if len(u[i])>len(max):
#         max=u[i]
#     i=i+1
# print(max)
# f.close()

# user=input("enter file name")
# f=open(user,"r")
# u=f.read().split("\n")
# k=u
# i=0
# while i<len(k):
#     i=i+1
# print(i)
# f.close()

# user=input("enter the file name")
# f=open(user,"r")
# lines=0
# words=0
# char=0
# for i in(f):
#     word_list=i.split("\n")
#     lines=lines+1
#     words=words+len(word_list)
#     char=char+len(i)
# print("line:",lines,"words:",words,"char:",char)