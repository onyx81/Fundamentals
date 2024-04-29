n = int(input())
chars = []
for _ in range(n):
    chars.append(input())
s = [ord(ch) for ch in chars]
print(f"The sum equals: {sum(s)}")