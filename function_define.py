def greet():
    print("Hello")
    print("Good Morning")


def add_sub(x, y):
    a = x + y
    b = x - y
    # print(a)
    return a, b


greet()
result1, result2 = add_sub(5, 7)
print(result1, result2)
