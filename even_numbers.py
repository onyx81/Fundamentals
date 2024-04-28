numbers = int(input())
all_numbers_even = True
for _ in range(numbers):
    number = int(input())
    if number % 2 != 0:
        print(f"{number} is odd!")
        exit()
print("All numbers are even.")
