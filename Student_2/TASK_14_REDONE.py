def sentenceChange(sentence, position):
    length = len(sentence)

    if length == 1 or position == 0:
        return sentence

    newString = ""
    tempString = ""
    total = 0
    for index in range(0,length):
        if index == 0:
            newString = newString + sentence[0]
            total += 1
            continue
        else:
            if index % position == 0:
                newString += sentence[index - position + 1: index]
                total += position
                tempString += sentence[index]
    if total != length:
        newString += sentence[total:length]

    newString = newString + tempString
    return newString


sentence = input()
position = int(input())
print(sentenceChange(sentence, position))
