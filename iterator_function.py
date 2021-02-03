nums = [5, 3, 8, 6, 4]

it = iter(nums)

print(it.__next__())   # will print the next element in list which is first in this case

print(next(it))        # will print the next element in list which is second in this case

for i in nums:         # will print all the elements of the list
    print(i)
