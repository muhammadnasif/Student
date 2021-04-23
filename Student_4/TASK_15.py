given = ([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12])

strReplace = input()

listConvert = list(given)

for data in listConvert:
    data[2] = strReplace

given = tuple(listConvert)

print(given)