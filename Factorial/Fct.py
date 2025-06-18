n=eval(input("enter any no: "))
fact = 1
for i in range(1, n + 1):
    fact *= i

print(fact)


# recurssion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Enter a number: "))
print(f"Factorial of {n} is {factorial(n)}")  