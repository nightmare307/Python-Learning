# -*- coding: utf-8 -*
#5.1条件测试
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')


#5.3外星人颜色#1
alien = 'red'
if alien == 'green':
    print('You get 5 points')
if alien != 'green':
    print('You get 1 point')

#5.4外星人颜色#2
aliens = 'green'
if aliens == 'green':
    print('You get 5 points')
else:
    print('You get 1 point')

aliens = 'red'
if aliens == 'green':
    print('You get 5 points')
else:
    print('You get 1 point')

#5.5外星人颜色#3
alienlist = ['green', 'yellow', 'red']
for alienc in alienlist:
    if alienc == 'green':
        points = 5
    elif alienc == 'yellow':
        points = 10
    elif alienc == 'red':
        points = 15
    print('You get %d points' % points)

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

#5.7喜欢的水果
favorite_fruits=['peach','orange','lemon','durian']
for fruit in favorite_fruits:
    print('You really like %s'%(fruit.title()))

#5.8以特殊方式和管理员打招呼
administrators = ['admin', 'chris', 'tiffany']
if administrators:
    for admin in administrators:
        if admin.lower() == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello %s, thank you for logging in again' % (admin.title()))
else:
    print('Please input user name')

#5.9处理没有用户的情形
administrators = []
if administrators:
    for admin in administrators:
        if admin.lower() == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print('Hello %s, thank you for logging in again' % (admin.title()))
else:
    print('Please input user name')
#5.10检查用户名
current_users = ['jack', 'CHris', 'betty', 'lizard', 'mariO', 'Lawson', 'bee']
new_users = ['JACK', 'Tiffany', 'Bee', 'nightmare']
#使用列表解析统一大小写
for user in new_users:
    if user.lower() in [current_user.lower() for current_user in current_users]:
        print('The name %s is used , please input another' % (user))
    else:
        print('The name %s is available' % (user))

#5.11序数
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for num in nums:
    if num == 1:
        print('%dst' % (num))
    elif num == 2:
        print('%dnd' % (num))
    elif num == 3:
        print('%drd' % (num))
    else:
        print('%dth' % (num))

