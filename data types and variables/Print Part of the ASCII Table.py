switch = True
start = int(input())
stop = int(input())
while switch:
    print(chr(start),end="")
    start += 1
    if start == stop:
        switch = False
    else:print(" ",end="")