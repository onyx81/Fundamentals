switch = True
start = int(input())
stop = int(input())
while switch:
    if start == stop:
        switch = False


    print(" ",end="")

    print(chr(start),end="")
    start += 1
