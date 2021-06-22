#dictionary

# alien = {'color':'green', 'num': 5}
# print(alien['color'])
# print(alien['num'])

#add key
# alien['x'] = 8
# alien['y'] = 2
# print(alien)

#change
# alien['color'] = 'blue'

# del key
# del alien['num']



#traverse dictionary
'''
for k,v in alien.items():
    print('key: ' + k)
    print('value: ' + str(v)) #only because value of num is int
'''

#travesre all key
# fav_language = {
#     'jac':'python',
#     'lina':'C',
#     'ks':'C++',
#     'phil':'java',
#     'pak':'C'
# }

'''
for i in fav_language.keys():
    print(i.title())
'''
#traverse key in order
# for i in sorted(fav_language.keys()):
#     print(i.title())

#traverse value
# for j in fav_language.values():
#     print(j.title())

## remove duplicate
# for a in set(fav_language.values()):
#     print(a.title())


### nest
ali_0 = {'color':'green', 'point':5}
ali_1 = {'color':'red', 'point':3}
ali_2 = {'color':'blue', 'point':1}
aliens = [ali_0, ali_1, ali_2]
for i in aliens:
    print(i)

# dictionary storage list
languages = {
    'mike':['java', 'C'],
    'linda':['python']
}