def add(a, *b):
    print(a)
    print(b)

    c = a

    for i in b:
        c = c + i

    print(c)


add(5, 6, 88, 54)
