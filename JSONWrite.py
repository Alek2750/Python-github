import json
numbers = {1: 'a', 2: [1,2,3]}
filename = 'test.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)