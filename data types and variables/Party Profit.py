import math

group_size = int(input())

days = int(input())

budget = 0

for day in range(days):
    day += 1
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5

    budget = budget + 50 - 2 * group_size

    if day % 3 == 0:
        budget -= 3*group_size
    if day % 5 == 0:
        budget += 20 * group_size
        if day % 3 == 0:
            budget -= 2 * group_size

target = budget / group_size

print(f"{group_size} companions received {math.floor(target)} coins each.")
