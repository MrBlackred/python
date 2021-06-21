
#case 1
# from car import Car

# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 12
# my_new_car.read_odometer()


# case 2
# from car import ElectricCar

# my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.fill_gas_tank()
# my_tesla.battery.describe_battery()


# case 3 
# import car

# my_new_car = car.Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.odometer_reading = 12
# my_new_car.read_odometer()


# my_tesla = car.ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.fill_gas_tank()
# my_tesla.battery.describe_battery()

# case 4
from car import * 
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 12
my_new_car.read_odometer()


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()