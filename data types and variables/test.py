number = int(input())
for i in range(1,number + 1):
    sum = 0
    n = i
    while n > 0:
        sum += n % 10
        n //= 10
    print(f"{i}->{sum in (5,7,11)}")