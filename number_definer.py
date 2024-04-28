n = "a"
num = float(input())
if num == 0:
    print("zero")
elif num < 0:
    n = "negative"
elif num > 0:
    n = "positive"
if abs(num) < 1 and num != 0:
    if n == "positive":
        print("small positive")
    elif n == "negative":
        print("small negative")
elif abs(num) > 1000000:
    if n == "positive":
        print("large positive")
    elif n == "negative":
        print("large negative")
else:
    if n == "positive":
        print("positive")
    elif n == "negative":
        print("negative")