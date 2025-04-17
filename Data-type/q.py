s1= 'python'

print(s1.index('t'))

print(s1.index("t"))
print(s1.index("h"))

# dict
l1=[10,20,30,'raj','jai',40]

# print(l1.index('10'))
print(l1.index('raj'))
print(l1.index(10))


# set  not support in set or frozen set
l2={10,20,30,"raj","jai"}
print(l2.index(10))


# index no
print(l1[2])


l=[10,20,30,40]

print(l.index(10))

l1=[10,20,30,40]

print(l1[2])
print(l1[2:5:-1])
print(l1[2:5:])

s="simit"
print(s[2:5:-1])

# reverse
print(s[::-1])


l1=[10,20,30,40,50,60,70,80]
print(l1[::-1])

print(l1[2:2])

print(l1[-3:-3:-1])


# negative direction

print(l[-2:-6])


# negative or postive index

print(l1[-6:5])

print(l1[1:-2])

# palindrom

# if(s==s[::--])

