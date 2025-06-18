# find simple interest 
def fun(p,r,t):
    return (p*r*t)/100

p=int(input("enter Principle Amount: "))
r=int(input("enter Rate of Interest: "))
t=int(input("enter Time : "))

res=fun(p,r,t)

print(res)


# lambda function 

si= lambda p,r,t:(p*r*t)/100

p=int(input("enter principle Amount: "))
r=int(input("enter Rate of Interest: "))
t=int(input("enter Time "))

res=si(p,r,t)
print(res)


# Using list comprehension


p=int(input("Enter any no: "))
r=int(input("Enter any no: "))
t=int(input("Enter any no: "))

si= [p*r*t/100] [0]
print(si)

