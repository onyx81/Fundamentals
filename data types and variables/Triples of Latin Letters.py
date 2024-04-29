n = int(input())
chars = []
for i in range(0,n):
    for k in range(0,n):
        for g in range(0,n):
            print(chr(97 + i)+chr(97 + k)+chr(97 + g))