#case 1
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

#case 2
# print("input two numbers, i'll divide them.")
# print("Enter 'q' to quit")

# while True:
#     first_num = input("first num: ")
#     if first_num == 'q':
#         break

#     sec_num = input("second num: ")
#     if sec_num == 'q':
#         break
#     try:
#         ans = int(first_num) / int(sec_num)
#     except ZeroDivisionError:
#         print("You can't divide by zero!")
#     else:
#         print(ans)


# case 3
filename = 'alice.txt'

try:
    with open(filename) as object:
        contents = object.read()
except FileNotFoundError:
    print("file do not exit.")
else:
    words = contents.split()
    num_words = len(words)
    print("This file has " + str(num_words) + " words!")