given = input()

given = given.replace(" ","")

result = {'1': [], '2': []}

for alphabet in given:
    if ord(alphabet) >= 48 and ord(alphabet) <= 57:
        result['1'].append(alphabet)
    else:
        result['2'].append(alphabet)

result['1'] = set(result['1'])
result['1'] = list(result['1'])

result['2'] = set(result['2'])
result['2'] = list(result['2'])


print(result)