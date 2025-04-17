# code reuseablity

def add(x,y):
    print(x+y)  #
    return(x+y)

p=int(input("enter any no:"))
q=int(input("enter any no:"))

print(add(p,q))
add(p,q)
z=add(p,q)
print(z)
print("hello")
print(z)

# even no


def Even(n):
    if n%2==0:
        print("even no")
    else:
        print("not a even no")
        

   
p=int(input("enter any no:"))

Even(p)


def Even(n):
    for i in range(2,n+1,2):
        print(i)
        

   
p=int(input("enter any no:"))

Even(p)

# odd
def Odd(n):
    for i in range(1,n,2):
        print(i)
        

   
p=int(input("enter any no:"))

Odd(p)
