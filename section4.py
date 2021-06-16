# operate list

'''
name = ['hh', 'sdq', 'sdw']
for i in name:
    print(i)
    print("hh no " + i)

print("gg wp\n")
'''

# creaet number list
'''
# no print 5 because range is [)
for value in range(1,5):
    print(value)

# put a list in variable
nums = list(range(1,5))
print(nums)

# set step in list
nub = list(range(1, 10, 2))
print(nub)

# clear version
seq = []
for i in range(1,11):
    seq.append(i**2)

print(seq)

# 4-3-3 sum() max() min()

### list analysis
pp = [j**2 for j in range(1,5)]
print(pp)
'''

## use part of list
team = ['ame', 'nts', 'faith_bian', 'xinq', 'y']
print(team[0:3])
print(team[1:4])
print(team[2:])
print(team[:2])
print(team[-2:])

for palyer in team[2:]:
    print(palyer.title())


## copy list 
psg_lgd = team[:]
print(psg_lgd)


## tuple
ggwp = (12, 2)
for i in ggwp:
    print(i)
