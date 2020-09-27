array1 = [121, 144, 19, 161, 19, 144, 19, 11]
array2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]


def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    elif array1 == array2:
        return True

    counter = 0
    new_lst_1 = []
    new_lst_2 = []
    new_lst_1a = [x for x in array1]
    new_lst_2a = [x for x in array2]

    for n in array1:
        if n*n in new_lst_2a:
            new_lst_1.append(n*n)
            counter += 1
            new_lst_2a.remove(n*n)
            if counter == len(array2) and len(new_lst_2a) == 0:
                return True

    counter = 0

    del new_lst_1[:]
    del new_lst_2a[:]

    for n in array2:
        if n*n in new_lst_1a:
            new_lst_2.append(n*n)
            counter += 1
            new_lst_1a.remove(n*n)
            if counter == len(array1) and len(new_lst_1a) == 0:
                return True
    return False


comp(array1, array2)
