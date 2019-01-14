# -*- coding: utf-8 -*
#6.1人
friend={'first_name':'tiffany',
        'last_name':'zhang',
        'age':28,
        'city':'beijing',}
print('My friend is %s %s ,she is %d years old , she is living in %s' % (
    friend['first_name'].title(), friend['last_name'].title(), friend['age'], 
	friend['city'].title()))

#6.2喜欢的数字
favnums={'jack':4,
        'rose':8,
        'john':3,
        'chris':4,
        'tiffany':2,}
for name,num in favnums.items():
    print("%s's favourite number is %d."%(name.title(),num))

#6.5河流
rivers={'nile':'egypt','amazon':'brazil','changjiang':'china'}
for river,nation in rivers.items():
    print('The %s runs through %s'%(river.title(),nation.title()))
for name in sorted(rivers.keys()):
    print(name.title())
for city in sorted(rivers.values()):
    print(city.title())

#6.6调查
favorite_languages = {'jen': 'python', 'sarah': 'c',
                      'edward': 'ruby', 'phil': 'python', }
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
investigate=['jen','jack','john','phil']
for invest in investigate:
    if invest in favorite_languages.keys():
        print('%s , Thank you for the investigation.'%(invest.title()))
    else:
        print('%s , please attend the investigation' % (invest.title()))

#6.7人
tiffany = {'first_name': 'tiffany',
          'last_name': 'zhang',
          'age': 28,
          'province':'beijing',
          'city': 'beijing', }
chris = {'first_name': 'chris',
         'last_name': 'li',
         'age': 30,
         'province': 'beijing',
         'city': 'beijing', }
dan = {'first_name': 'dan',
        'last_name': 'zhang',
        'age': 26,
        'province': 'hebei',
        'city': 'chengde', }
people=[tiffany,chris,dan]
for one in people:
	print(one)
