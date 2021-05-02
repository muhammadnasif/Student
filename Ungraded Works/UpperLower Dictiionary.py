def stringCount(string):
    countDictionary = {}

    dictionary_result = {}
    uniqueElem = string.lower()
    uniqueElem = set(uniqueElem)

    for alphabet in string:
        if alphabet not in countDictionary:
            countDictionary[alphabet] = 1
        else:
            countDictionary[alphabet] += 1

    for elements in uniqueElem:
        if elements.upper() in countDictionary:
            dictionary_result[elements] = []
            dictionary_result[elements].append(countDictionary[elements])
            dictionary_result[elements].append(countDictionary[elements.upper()])

    return dictionary_result


inputString = input()
print(stringCount(inputString))
