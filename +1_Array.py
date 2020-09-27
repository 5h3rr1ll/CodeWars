arr = [9, 10, 0]


def up_array(arr):

    if arr == []:
        return None

    lst2 = []
    r_sum = 0

    for n, i in zip(arr, range(1, len(arr) + 1)):
        if n not in range(0, 10):
            return None
        n = n * int("1" + "".zfill(len(arr) - i))
        lst2.append(n)

    r_sum = sum(lst2) + 1

    return [int(x) for x in str(r_sum)]


up_array(arr)
