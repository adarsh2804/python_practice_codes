def sort(ls):

    for i in range(0, len(ls) - 1):
        minpos = i

        for j in range(i, len(ls)):
            if ls[j] < ls[minpos]:     # comparing elements of unsorted(remaining) array with minimum value
                minpos = j

        temp = ls[i]
        ls[i] = ls[minpos]
        ls[minpos] = temp

        print(ls)


lst = [5, 3, 8, 6, 7, 2, 9, 4]
sort(lst)

print(lst)

# Adding this line from github
