given = {'a': 6, 'b': 7, 'c': 9, 'd': 8, 'e': 11, 'f': 12, 'g': 13}

input_str = input()

new = input_str.split(",")

val_1 = int(new[0].strip())
val_2 = int(new[1].strip())

if val_1 > val_2:
    high = val_1
    low = val_2
else:
    high = val_2
    low = val_1

result_dictionary = {}

for key, value in given.items():
    if value >= low and value < high:
        result_dictionary[key] = value

print(result_dictionary)
