lst = "12 ,17, 79, 103, 36, 97, 71 , 44, 77, 90"

result = {'lucky':[],'unlucky':[]}


lst = lst.split(",")
limit = len(lst)
inserted = False
for i in range(0, limit):
    lst[i] = lst[i].strip()
for number in lst:
    for digit in number:
        if digit == '7':
                result['lucky'].append(int(number))
                inserted = True
                break
    if not inserted:
        result['unlucky'].append(int(number))
    inserted = False

print(result)