def tensquare():

    n = 1

    while n <= 10:
        sq = n * n
        yield sq         # it will fetch the value one by one while return will terminate the loop
        n += 1


values = tensquare()

for i in values:
    print(i)
