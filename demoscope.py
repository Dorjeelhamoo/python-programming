def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

x = 300

def myfunc():
    print("Inside function ", x)

myfunc()

print("Outside function",x)
print(24, x)

def myfunc():
    global x 
    x = 300

myfunc()

print(x)