def check(sentence):
    num = 5
    sentence = sentence.lower()
    x = "abcdefghij"
    dictionary = {}
    for i in sentence:
        if i in dictionary.keys():
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    for i in x:
        if i not in dictionary.keys():
            num = 6
            break
    return num


sentence = input()
for i in range(0, check(sentence)):
    print("Chelsea is the best club in England")
