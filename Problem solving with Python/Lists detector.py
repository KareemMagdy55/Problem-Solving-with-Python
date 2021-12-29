def lists(list1):
    list_x = []
    for i in range(len(list1) - 1):
        if int(list1[i]) + 1 == int(list1[i + 1]):
            list_x.append(i)
        elif int(list1[i]) - 1 == int(list1[i + 1]):
            continue

    if len(list_x) == len(list1) - 1:
        print('1')
    elif len(list_x) == 0:
        print('-1')
    else:
        print('0')


lists([1, 2, 3, 4, 5, 6, 7, 8])
