def lists_equal(list1, list2):
    sum1 = 0
    sum2 = 0
    for i in range(len(list1)):
        sum1 = sum1 + list1[i]
        sum2 = sum2 + list2[i]
    if sum1 / sum2 == 1:
        print('Lists are equal', '=', True)
    else:
        print('Lists are equal', '=', False)


lists_equal([1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1])

# Same code with built-in function
# def lists_equal(list1, list2):
#     if sum(list1) / sum(list2) == 1:
#         print('Lists are equal', '=', True)
#     else:
#         print('Lists are equal', '=', False)
#
#
# lists_equal([1, 2, 3, 4, 5, 6, 7, 8], [8, 7, 6, 5, 4, 3, 2, 1])
