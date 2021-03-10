# write your code here
import json
with open('users.json') as json_file:
    print(len(json.load(json_file)['users']))
