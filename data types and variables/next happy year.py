year = int(input())
happy = False
while not happy:
    year += 1
    number = year
    digits = []
    while number > 0:
        d = number % 10
        number //= 10
        digits.append(d)

    for _ in range(1,len(digits) + 1):
        ch = digits.pop()
        if ch in digits:
            break
    else:
        print(year)
        happy = True