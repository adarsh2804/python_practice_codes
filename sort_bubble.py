
def sort(ls):
    for i in range(len(ls) - 1, 0, -1):     # outer loop runs in decreasing order
        for j in range(i):      # will run till one position less everytime since greatest no. is fixed at last position
            if ls[j] > ls[j + 1]:
                temp = ls[j]
                ls[j] = ls[j + 1]
                ls[j + 1] = temp


lst = [5, 3, 8, 6, 7, 2]
sort(lst)

print(lst)
