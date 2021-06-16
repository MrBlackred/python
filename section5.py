# if
cars = ['audi', 'bmw', 'benc']
for i in cars:
    if i == 'audi':
        print(i.title())
    else:
        print(i.upper())

c1 = "sda"
if c1 != "sdaw":
    print("ok")

num = 13
if num != 20:
    print("HH")

# multiple conditions  use and


# no in condition
car = "Jeep"
if car not in cars:
    print(car.title() + "is no BBA")

age = 12
if age < 4:
    print("free")
elif age < 18:
    print("half fare")
else:
    print("No discount")


empty = []
if empty:
    for i in empty:
        print(i.title())
else:
    print("is empty")