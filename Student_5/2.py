sentence = input()

result = {}

position = 0
for char in sentence:
    if char in result.keys():
        result[char].append(position)
    else:
        result[char] = []
        result[char].append(position)
    position += 1

del result[' ']

print(result)