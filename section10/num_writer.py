import json

file_name = 'num.json'
# numbers = [2, 3, 4, 5, 6]
# with open(file_name, 'w') as object:
#     json.dump(numbers, object)

with open(file_name) as f_obj:
    numbers = json.load(f_obj)

print(numbers)