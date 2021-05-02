def splitEmail(eList):
    result_dictionary = {}

    for email in eList:
        email = email.replace(".com", "")
        part = email.split("@")
        if part[1] not in result_dictionary:
            result_dictionary[part[1]] = []
            result_dictionary[part[1]].append(part[0])
        else:
            result_dictionary[part[1]].append(part[0])

    return result_dictionary


num = int(input())
newList = []
for i in range(0, num):
    val = input()
    newList.append(val)

print(splitEmail(newList))
