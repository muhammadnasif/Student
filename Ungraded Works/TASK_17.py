def remove_odd(lst):
    newList = []
    for data in lst:
        if data % 2 == 0:
            newList.append(data)
    lst = newList
    return lst

lst = [1,23,44,565,78,66,77]
print(remove_odd(lst))