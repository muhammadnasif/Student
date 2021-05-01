def func(start, end, first, second):
    sum=0
    for i in range(start, end):
        if i % first == 0 and i % second != 0:
            sum += i
        elif i % first != 0 and i % second == 0:
            sum += i

    return sum

start = int(input())
end = int(input())
div_first = int(input())
div_second = int(input())

print(func(start, end, div_first, div_second))
