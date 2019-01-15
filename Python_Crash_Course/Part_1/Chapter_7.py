# -*- coding: utf-8 -*
#7.1汽车租赁
car=input('What\'s car do you want ?\n')
print('Let me see if I can find you a %s.'%(car))

#7.2餐馆定位
count=int(input('How many peoples will have dinner ?\n'))
if count > 8:
    print('There is not have a big enough table !')
else:
    print('All of you welcome here!')

#7.3 10的整数倍
num = int(input('Please input a number:\n'))
if num == 0:
    print('The number must bigger than 0,input again')
    num = int(input('Please input a number:\n'))
elif num%10=='0':
    print('The number is correct!')
else:
    print('The number is wrong')

#7.4食物配料
prompt= '\nPlease select something to add into your burger :\nEnter \'quit\' when you are ready:\n'
food=''
while food != 'quit':
    food = input(prompt)
    if food != 'quit':
        print('Ok , We will add %s into your burger!'%(food))

#7.5电影票
age=''
price=''
while age != 'quit':
        age = input('\nPlease input your age :\nEnter \'quit\' when you need quit\n')
        if len(age) >3:
            break
        elif int(age) < 3:
            price='free'
            print('Your ticket price is %s' % (price))
        elif int(age)<=12:
            price='10$'
            print('Your ticket price is %s' % (price))
        elif int(age) >12:
            price='15$'
            print('Your ticket price is %s' % (price))

