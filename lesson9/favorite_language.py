from collections import OrderedDict

favorite_laguages = OrderedDict()

favorite_laguages['jen'] = 'python'
favorite_laguages['sarah'] = 'c'
favorite_laguages['edsard'] = 'ruby'
favorite_laguages['phil'] = 'java'

for name, language in favorite_laguages.items():
    print(name.title() + "'s favorite language is " + language.title())

