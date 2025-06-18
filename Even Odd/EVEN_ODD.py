# Even Odd 
n=int(input("Enter any number: "))

if n%2==0:
    print("Even")

else:
    print("Odd")

# Use lambda with map
a = [1, 2, 3, 4, 5]

res = map(lambda num: str(num) + " Even" 
          if num % 2 == 0 else str(num) + " Odd", a)

print("\n".join(res))


# Using Bitwise And(&) Operator

a=int(input("Enter any no: "))

if a & 1==0:
    print("Even")

else:
    print("Odd")


# 