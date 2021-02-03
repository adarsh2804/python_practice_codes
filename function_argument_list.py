def update(lst):
    print(id(lst))
    lst[1] = 25
    print(id(lst))
    print("x = ", lst)


lst = [10, 44, 43]
print(id(lst))
update(lst)
print("lst = ", lst)
