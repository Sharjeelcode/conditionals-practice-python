# mydict = {
#     'name':'sharjeel',
#     'fname' : 'aziz'
# }

# mydict['name'] = 'Ahmed'

# for keys in mydict:
#     print(f'my {keys.capitalize()} is {mydict[keys].capitalize()}')
# # print(mydict)

# for keys, values in mydict.items():
#     print(f'my {keys} is {values}')

# if 'names' in mydict:
#     print('yes')
# elif 'fname' in mydict:
#     print('yes')
# else:
#     print('both no')

# print(mydict.popitem())

# print(mydict)

# teaShop = {
#     'chai':{'masala':'spicy','ginger':'ajeeb'},
#     'tea':{'drak':'tea'}
# }

# print(teaShop['chai']['masala'])


# squareNums = {x:x**2 for x in range(1,10)}

# print(squareNums)


teas = ['masala','lemon','ginger','kashmiri']
taste = 'delicious'

aboutTea = dict.fromkeys(teas,taste)

print(aboutTea)


