from functools import reduce

# def is_even(n):
# return n % 2 == 0

# def update(n)
# return n+2

# def add_all(a, b):
#    return a + b

nums = [1, 3, 5, 4, 8, 6, 2]

evens = list(filter(lambda n: n % 2 == 0, nums))
print(evens)

doubles = list(map(lambda n: n * 2, evens))
print(doubles)

sums = reduce(lambda a, b: a + b, doubles)
print(sums)
