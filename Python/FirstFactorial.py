def factorial (n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(4)) #  24
print(factorial(8)) # 40320
print(factorial(9)) # 362880
print(factorial(12)) # 479001600