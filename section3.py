# list

'''
name = ['ame', 'nts', 'fb', 'XQ', 'y']
print(name)
print(name[0].title())
print(name[-1])  # end element

## 3-2  append change del insert
name[0] = 'kaka'  #change
name.append('hel')
name.insert(0, 'lx')

name2 = name.pop()
name3 = name.pop(2)
name.remove('kaka')
del name[1]
print(name)
print(name2)
print(name3)
'''

## sort
cars = ['bmw', 'audi', 'tyt', 'sbr']
# cars.sort() #forver
print(cars)
# temporary
print(sorted(cars))
print(cars)
cars.reverse()
print(cars)