book_list = {'Pride and Prejudice': 1500, 'Alchemist': 800, 'Frankenstein': 900, 'The Great Gatsby': 750}

cash = int(input())

total = 0
for value in book_list.values():
    total += value

print("Sum = "+str(total))
if cash < total:
    print("Not enough money please give a larger input")
else:
    print("Happy Reading!!!")