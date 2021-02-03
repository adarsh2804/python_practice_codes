def person(name, **data):

    print(name)
    print(data)

    for i, j in data.items():
        print(i, j)


person('adarsh', age=24, city='shajapur', mob=9876543)
