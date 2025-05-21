# file handing
f=open('n1.py', 'x')
# mode x
f=open('n3.py', 'x')
print("file created")

print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
print(f.closed)
f.close()
print(f.closed)

# mode w
# it file contain delete
f=open('n3.py', 'w')
print("file created")
print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
print(f.closed)
f.close()
print(f.closed)


# you can read a file in w mode 
f=open('n4.py', 'w')
print("file created")
print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
print(f.closed)
f.close()
print(f.closed)


# read mode 

# f=open('n4.py','r')

print("file created")
print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
print(f.closed)
f.close()
print(f.closed)


# append mode 

f=open('x1.py','a')

print("file created")
print(f.name)
print(f.mode)
print(f.readable())
print(f.writable())
print(f.closed)
f.close()
print(f.closed)


