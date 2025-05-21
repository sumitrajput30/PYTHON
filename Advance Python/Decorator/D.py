# Decorator

def decor(fun):
    def inner():
        fun()
    return 5
    
def mainfun():
    print("main function")

x=decor(mainfun)
print(x)
x()

# inner

def decor():
    def inner():
        print("hello")
    return inner

x=decor()
print(x)
x()




def decor(z):
    def inner(x,y):
        print(x+y)
        print(z)
    return inner

x=decor(10)
p=int(input("enter any no:"))
q=int(input("enter any no:"))
x(p,q)
