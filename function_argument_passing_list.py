def count(lst):

    even = 0
    odd = 0

    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


c = [3, 6, 8, 5, 9, 33, 87, 54]

a, b = count(c)

print("Even : {} and Odd : {}".format(a, b))
