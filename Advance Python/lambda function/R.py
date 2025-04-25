# lambda function


x = lambda p,q : p+q

r=int(input("enter any no:"))
s=int(input("enter any no:"))
x(r,s)
print(x(r,s)+5)
z=x(r,s)
print(z+14)

# lambda with map

l=[2,4,5,48,4,84,7]
x=list(map(lambda x: x**2 , l))

print(x)

# even no

l=[1,2,3,4,5,6,7,8,9]
x=list(filter(lambda x: x if x%2==0 else None , l))
x=list(filter(lambda x:  x%2==0  , l))

print(x)

# reduce 
import functools
l=[1,2,3,4,5,6,7,8,9]

x=functools.reduce(lambda x,y : x+y , l)
x1=functools.reduce(lambda x,y : x if x>y else y, l)
x2=functools.reduce(lambda x,y : x if x<y else y, l)

print(x)
print(x1)
print(x2)