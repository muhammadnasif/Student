def rem_duplicate(lst):
    uniqueElements = set(lst)

    sum = 0
    newList = []
    for data in uniqueElements:
        value = lst.count(data)
        if value > 2:
            sum += (value - 2)
            newList.append(data)
            newList.append(data)
        elif value == 2:
            newList.append(data)
            newList.append(data)
        elif value == 1:
            newList.append(data)

    return sum, newList


lst = [10, 10, 15, 15, 20]
removed, newList = rem_duplicate(lst)
print("Removed " + str(removed))
print(newList)
