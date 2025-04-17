# dictionary 

d={'name':'Sumit','age':21,'qaulification':'B..tech'}
print(d)
print(type(d))


# len
print(len(d))
# max
print(max(d))
# min
print(min(d))
# type
print(type(d))
# id
print(id(d))

# methods

# clear
# d.clear()
# print(d)

# copy
x=d.copy()
print(x,d)
print(id(x), id(d))

# fromkeys
l=["name", 'age', "quali"]
d1=dict.fromkeys(l)
print(d1)

l1="sumit"
d2=dict.fromkeys(l1,1)
print(d2)

# get
print(d.get("age"))

# items

print(d.items())

# keys

print(d.keys())

# values

print(d.values())

# pop()

# print(d.pop("name"))

# popitem

# print(d.popitem())

# setdefault

print(d.setdefault("name","rajput"))

print(d.setdefault("q","rajput"))

# update

d2={"gread":"m.tech", "city":"bhopal"}
d.update(d2)
print(d)

# update
d["name"]="Amit"
print(d)

# read
print(d["name"])

# create
d["gred"]="m.tech"
print(d)



