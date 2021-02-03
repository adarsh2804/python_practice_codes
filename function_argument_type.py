def person(name, age=18):
    print(name)
    print(age)


person('adarsh', 24)  # 18 is replaced by argument user give
person(age=24, name='adarsh')  # keyword argument
person('adarsh')  # default argument as 18 is assigned already


