n=int(input("enter any no:"))

for x in range(1,n+1,):
    print(x)


# even
n=int(input("enter any no:"))

for x in range(2,n+1,2):
    print(x)


# odd
n=int(input("enter any no:"))

for x in range(1,n+1,2):
    print(x)

# print 10 even no

n=int(input("enter any no:"))

for x in range(1,n+1):
    print(2*x, end=",")


# # print 10 odd no 

n=int(input("enter any no:"))

for x in range(1,n+1):
    print(2*x-1, end=",")


# sum even or odd  or 10 tak 10 



# sum even no

n=int(input("enter any no:"))
sum=0
for x in range(2,n+1,2):

    print(x) 
    sum+=x

print(sum)


# 10 even no sum

n=int(input("enter any no:"))
sum=0
for x in range(1,n+1):
    print(2*x, end=",")
    sum+=x

print("sum=",sum)


# odd 

n=int(input("enter any no:"))
sum=0
for x in range(1,n+1,2):
    print(x)
    sum+=x

print("sum=",sum)

# 10 odd no

n=int(input("enter any no:"))
sum=0
for x in range(1,n+1):
   print(2*x-1, end=",")
  
   sum+=x

print("sum=",sum)

