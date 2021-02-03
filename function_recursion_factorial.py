def factorial(n):

    if n == 0:
        return 1

    return n * factorial(n - 1)


x = int(input("Enter the number : "))
result = factorial(x)
print(result)
