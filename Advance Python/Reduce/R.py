import functools
l=[1,2,3,4,5,9,7]
def sum(x,y):
    return x+y

x=functools.reduce(sum,l)
print(x)


# max
l1=[1,2,3,4,5,9,7]
def max(x,y):
    if x>y:
        return x
    else:
        return y
   

x=functools.reduce(max,l1)
print(x)

# min

l1=[1,2,3,4,5,9,7]
def min(x,y):
    if x<y:
        return x
    else:
        return y
   

x=functools.reduce(min,l1)
print(x)



