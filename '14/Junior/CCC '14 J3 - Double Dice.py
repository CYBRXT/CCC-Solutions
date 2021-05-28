numberofrounds = int(input())

ascoretotal = 100
dscoretotal = 100

for i in range(numberofrounds):
    rolls = list(map(int, input().split(" ")))

    a_roll = rolls[0]
    d_roll = rolls[1]

    if a_roll < d_roll:
        ascoretotal = ascoretotal - d_roll
        dscoretotal = dscoretotal
    elif a_roll > d_roll:
        dscoretotal = dscoretotal - a_roll
        ascoretotal = ascoretotal
    else:
        pass

print(ascoretotal)
print(dscoretotal)