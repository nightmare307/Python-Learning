# -*- coding: utf-8 -*
#5.1条件测试
car = 'subaru' 
print("Is car == 'subaru'? I predict True.") 
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.") 
print(car == 'audi')


#5.3外星人颜色#1
alien='red'
if alien=='green':
    print('You get 5 points')
if alien != 'green':
    print('You get 1 point')

#5.4外星人颜色#2
aliens='green'
if aliens=='green':
    print('You get 5 points')
else:
    print('You get 1 point')

aliens='red'
if aliens == 'green':
    print('You get 5 points')
else:
    print('You get 1 point')

#5.5外星人颜色#3
alienlist=['green','yellow','red']
for alienc in alienlist:
    if alienc == 'green':
        points=5
    elif alienc == 'yellow':
        points=10
    elif alienc=='red':
        points=15
    print('You get %d points'%points)

#5.6人生的不同阶段
age=3
if age < 2:
    print('He(She) is a baby')
elif age < 4:
    print('He(She) is a kid')
elif age < 13:
    print('He(She) is a junior')
elif age < 20:
    print('He(She) is a youth')
elif age < 65:
    print('He(She) is a adult')
else:
    print('He(She) is an aged')

