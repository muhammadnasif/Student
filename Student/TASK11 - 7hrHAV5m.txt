def rem_duplicate(tpl):
    lst = list(tpl)
    newList = []
    push = True
    currentPosition = 0
    for data_1 in lst:
        push = True
        for data_2 in newList:
            if data_2 == data_1:
                push = False
                break

        if push == True:
            newList.append(data_1)
    tpl = tuple(newList)
    return tpl


lst = (1, 1, 1, 2, 3, 4, 5, [7, 7, 7, 5], [7, 7, 8, 5], [7, 7, 7, 5])
print(rem_duplicate(lst))
