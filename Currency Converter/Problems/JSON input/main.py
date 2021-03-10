import json


# write your code here
json_string = input()
json_dict = json.loads(json_string)
print(type(json_dict))
print(json_dict)
