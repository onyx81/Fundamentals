n_lines = int(input())

for i in range(n_lines):
    message = int(input())
    if message == 88:
        print("Hello")
    elif message == 86:
        print("How are you?")
    elif message < 88:
        print("GREAT!")
    elif message > 88:
        print("Bye.")