def cal_bonus(*args):
    length = int(len(args) / 4)

    for i in range(0, length):
        name = args[4 * i]
        salary = args[4 * i + 1]
        goal = args[4 * i + 2]
        bonus = args[4 * i + 3]
        defaultBonus = 0
        if goal > 30:
            defaultBonus = 10000
        elif goal >= 20 and goal <= 30:
            defaultBonus = 5000

        total = goal * ((bonus / 100) * salary) + defaultBonus
        print(name + " earned a bonus of " + str(total) + " Taka for " + str(goal) + " goals.")

cal_bonus("Neymar", 1200000, 35, 5, "Jamal", 700000, 19, 5)
#           0           1    2   3    4      5       6   7
#          4*i+0      4*i+1  4*i+2 4*i+3 4*i+0  4*i+1  4*i+2 4*i+3