class Student:

    def __init__(self, *args):
        self.name = args[0]
        self.last_name = args[1]
        self.birth_year = args[2]
        # calculate the student_id here
        self.student_id = self.name[0] + self.last_name + self.birth_year


input_data = []
for i in range(3):
    input_data.append(str(input()))

child = Student(*input_data)
print(child.student_id)
