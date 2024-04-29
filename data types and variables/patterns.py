num = int(input())
n=1
for n in range(1,num + 1):
    for _ in range(n):
        print("*",end="")
    print("")
for n in range(num - 1,0,-1):
    for _ in range(n):
        print("*",end="")
    print("")


