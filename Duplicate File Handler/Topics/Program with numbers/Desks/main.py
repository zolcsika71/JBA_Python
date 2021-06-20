import math

desks = 0

for i in range(3):
    student_number = int(input())
    desks += math.ceil(student_number / 2)

print(desks)


