filename = 'pi_digits.txt'
# with open(filename) as file_object:
#     # contents = file_object.read()
#     # print(contents)

#     for line in file_object:
#         print(line)

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

# print(pi_string)
# print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Yeh")
else:
    print("ha")