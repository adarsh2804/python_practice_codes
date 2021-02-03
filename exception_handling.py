a = 5
b = 3

try:
    print("Resource open")
    print(a/b)

    k = int(input("Enter the number : "))
    print(k)

except ZeroDivisionError as e:
    print("Cannot divide the number by zero", e)

except ValueError as e:                  # e will show the error
    print("Type of input is wrong")

except Exception as e:                   # will except all other exceptions
    print("Something went wrong...")

finally:                                 # will run no matter there is an exception or not
    print("Resource closed")

print("bye")
