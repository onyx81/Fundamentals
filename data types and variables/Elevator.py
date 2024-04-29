from math import ceil

num_people = int(input())
capacity_people = int(input())

courses = num_people // capacity_people
if num_people % capacity_people == 0:
    print(courses)
else:
    print(courses + 1)
#print(ceil(courses))
