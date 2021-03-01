lst = [4, 7, 8, 12, 45, 99]
n = 9
pos = 0


def bsearch(ls, n):

    l = 0
    u = len(ls) - 1

    while l <= u:
        mid = (l + u) // 2

        if ls[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if ls[mid] < n:
                l = mid + 1
            else:
                u = mid - 1

    return False


if bsearch(lst, n):
    print("found at position ", pos + 1)
else:
    print("Not found")
