# The following code is needed for us to check your answer, do not modify it, please.
students = json.loads(input())
Belov = students['Belov']
Smith = students['Smith']
Sarada = students['Sarada']

# Your code here. Work with the variables 'Belov', 'Smith', and 'Sarada'
unique_set = set()
unique_set.update(Belov)
unique_set.update(Smith)
unique_set.update(Sarada)

print(len(unique_set))
