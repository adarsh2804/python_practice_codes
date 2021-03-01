lst = [5, 8, 4, 6, 9, 2]
n = 9
pos = 0


def search(lst, n):
    i = 0

    while i < len(lst):
        if lst[i] == n:
            globals()['pos'] = i
            return True

        i += 1

    return False


if search(lst, n):
    print("found at ", pos + 1)
else:
    print("Not found")
