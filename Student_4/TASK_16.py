my_dictionary = {'c1': 'Red', 'c2': 'Green', 'c3': None, 'd4': 'Blue', 'a5': None}

removeElem = []

for key, value in my_dictionary.items():
    if value is None:
        removeElem.append(key)

for data in removeElem:
    del my_dictionary[data]

print(my_dictionary)