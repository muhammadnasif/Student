givenList = [(20, 80), (31, 80), (1, 22), (88, 11), (27, 11)]
result_dictionary = {}

for data in givenList:
    key = data[1]
    value = data
    if key in result_dictionary.keys():
        result_dictionary[key].append(value)
    else:
        result_dictionary[key] = []
        result_dictionary[key].append(value)

print(result_dictionary)