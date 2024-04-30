capacity = 255
current_volume = 0
number_of_lines = int(input())
for _ in range(number_of_lines):
    liters = int(input())
    if capacity >= liters:
        capacity -= liters
        current_volume += liters
    else:
        print("Insufficient capacity!")

print(current_volume)
