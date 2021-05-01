def calculate(value, note):

    counter = int(value/note)
    rem = value % note

    return counter, rem


def splitMoney(value):
    t500, value = calculate(value, 500)
    t100, value = calculate(value, 100)
    t50, value = calculate(value, 50)
    t20, value = calculate(value, 20)
    t10, value = calculate(value, 10)
    t5, value = calculate(value, 5)
    t2, value = calculate(value, 2)
    t1 = value

    return t500, t100, t50, t20, t10, t5, t2, t1


money = int(input())
result = splitMoney(money)
if result[0] > 0:
    print("500 taka: " + str(result[0]) + " note(s)")
if result[1] > 0:
    print("100 taka: " + str(result[1]) + " note(s)")
if result[2] > 0:
    print("50 taka: " + str(result[2]) + " note(s)")
if result[3] > 0:
    print("20 taka: " + str(result[3]) + " note(s)")
if result[4] > 0:
    print("10 taka: " + str(result[4]) + " note(s)")
if result[5] > 0:
    print("5 taka: " + str(result[5]) + " note(s)")
if result[6] > 0:
    print("2 taka: " + str(result[6]) + " note(s)")
if result[7] > 0:
    print("1 taka: " + str(result[7]) + " note(s)")

