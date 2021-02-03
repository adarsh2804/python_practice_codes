a = 10
print(id(a))


def something():
    # print(id(a))
    # global a

    a = 15
    x = globals()['a']
    print(id(x))
    print('x = ', x)

    # b = 8
    print('in fun ', a)
    print(id(a))

    globals()['a'] = 6


something()
print('out fun', a)
print(id(a))
# print(b)
