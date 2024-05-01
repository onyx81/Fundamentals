max_row = int(input())

for k in range(1,max_row + 1):
    print(k*"*")
for t in range(max_row-1,0,-1):
    print(t * "*")