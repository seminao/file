batch1= ["Shivam", "Rahul", "Kavay", "Dhannu", "Deepanshu", "Nitin", "Manoj"]
f= open("student name", "w")
for student in batch1:
    f.write(student+"\n")
f.close()
