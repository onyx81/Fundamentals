quantity_snowballs = int(input())
max_value = 0

for bal in range(1,quantity_snowballs + 1):
    weight = int(input())
    time_needed = int(input())
    quality = int(input())
    value = (weight // time_needed) ** quality
    if max_value < value:
        max_weight = weight
        min_time = time_needed
        max_quality = quality
        max_value = value

print(f"{max_weight} : {min_time} = {max_value} ({max_quality})")