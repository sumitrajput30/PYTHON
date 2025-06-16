# min 

a=input("enter any no: ")
b=input("enter any no: ")


print(min(a,b))

# using condition statement 

a=input("Enter any no: ")
b=input("Enter any no: ")

if a<b:
    print(a)

else:
    print(b)

# ternary operator

a=input("Enter any no: ")
b=input("Enter any no: ")

print(a if a<b else b)

# sort method 



a = input("Enter any number: ")
b = input("Enter any number: ")

res = list(str(a) + str(b))  
res = [int(i) for i in res]  
res.sort()                  

res1 = res[-1] - res[0]     
print("Result after subtraction:", res1)