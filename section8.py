#function

def greet_user(name):
    print("Hello, " + name.title() + "!")


# greet_user('jack')

def describe_pet(type, name = 'kaka'):
    print("I have a " + type + ": " + name.title())

# describe_pet('dog', 'uu')
# describe_pet(type='cat', name='mimi')
# describe_pet(name='tom', type='cat')

#default parameter must be 2th
# describe_pet('monkey')


# 8-3
def get_formatted_name(first_name, last_name, midle_name=''):
    if midle_name:
        full_name = first_name + " " + midle_name +' ' + last_name
    else:
        full_name = first_name + " " + last_name
    return full_name.title()

# print(get_formatted_name('jimi', 'hendriix'))
# print(get_formatted_name('john', 'hooker', 'lee'))


def build_name(first_name, last_name):
    person = {'first': first_name, 'last' : last_name}
    return person

# print(build_name('jimi', 'hooker'))


def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print('Printing model: ' + current_design)
        completed_models.append(current_design)

def show_models(completed_models):
    print("\nThe following models have been printed:")
    for i in completed_models:
        print(i)

a = ['iphone case', 'robot pendant', 'dodecahedrom']
b = []


# print_models(a, b)
#create a copy, without changing the original value
# print_models(a[:], b)
# show_models(b)


# 8-5 pass any number of parameters
def make_pizza(size, *toppoings):
    print("pizza size is " + str(size) + '\n')
    for toppoing in toppoings:
        print("- " + toppoing)

# make_pizza(12, 'beef', 'milk')

## input any number dictionarys
def build_profile(first, last, **userinfo):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in userinfo.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'sdaddd',
                            location = 'kd',
                            filed = 'physics')

print(user_profile)