class topten:

    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self                # it will give object of iterator

    def __next__(self):            # it will give the next object

        if self.num <= 10:         # will iterate till the value is 10
            val = self.num
            self.num += 1

            return val
        else:
            raise StopIteration    # it will stop the iterator otherwise iterator will run infinite times


values = topten()

# print(values.__next__())
print(values.__next__())
print(next(values))

for i in values:
    print(i)
