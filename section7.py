## input and while   use

# msg = input("input a message:")
# print(msg)

#msg too long 
# prompt = "If you tell us who you are, we can tell something."
# prompt += "\nSo what's your name?   "

# name = input(prompt)
# print(name)

# int()
# age = input("How old are you? \n")
# age = int(age)

# if age >= 18:
#     print("You are a grown man now")
#     print("google: You are already an adult")
# else:
#     print("HI")


####    while

# n = 1
# while n < 5:
#     print(n)
#     n += 1



## quit while
# msg = "input something: "
# mm = ""
# while mm != 'quit':
#     mm = input(msg)
#     print(mm)

# msg = "HAAAAAAAAAAAA,"
# msg += "  input some:  "

# active = True
# while active:
#     po = input(msg)

#     if po == 'quit':
#         active = False 
        # or 
        # break
    # else:
    #     print(msg)

# continue
number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        print(number)
    else:
        continue