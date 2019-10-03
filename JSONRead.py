import json
filename = 'test.json'
with open(filename) as f_obj:
    de_numbers = json.load(f_obj)
print(de_numbers)