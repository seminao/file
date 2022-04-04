def fun():
    import os
    if os.path.exists("name"):
        os.remove("name")
    else:
        print("no file exist")
fun()