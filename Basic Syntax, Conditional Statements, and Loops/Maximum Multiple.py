divisor = int(input())
boundary = int(input())
for _ in range(boundary):
    if boundary % divisor == 0:
        print(boundary)
        break
    else:
        boundary -= 1
