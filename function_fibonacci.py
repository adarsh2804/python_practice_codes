def fib(n):
    a = 0
    b = 1
    i = 3

    if n == 1:
        print(a)

    else:
        print(a)
        print(b)

        while i <= n:  # for i in range(2,n)
            c = a + b
            print(c)
            a = b
            b = c
            i += 1


x = (int(input("Enter the number of terms : ")))
fib(x)
