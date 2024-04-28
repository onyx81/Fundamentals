word = input()
n = 1
for char in word:
    print(word[len(word)-n],end="")
    n += 1