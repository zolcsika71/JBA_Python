# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']
# your code here

groups_dict = dict.fromkeys(groups)

number_of_groups = int(input())

students_number = []

for i in range(number_of_groups):
    students_number.append(int(input()))

for i in range(len(students_number)):
    groups_dict[groups[i]] = students_number[i]

print(groups_dict)
