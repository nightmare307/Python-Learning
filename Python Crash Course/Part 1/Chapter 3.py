# -*- coding: utf-8 -*
#3.1嘉宾名单
names=['Jack','Rose','Jay','John']
print(names)
print(names[0])
print(names[1])
print(names[2])
print(names[3])
#3.2问候语
print('Hi , '+names[0]+' , I invite you.')
print('Hi , '+names[1]+' , I invite you.')
print('Hi , '+names[2]+' , I invite you.')
print('Hi , '+names[3]+' , I invite you.')
#3.3自己的列表
cars=['Nissan','Benz','BMW','Toyota']
print('I would like to own a '+cars[0]+' car.')
#3.4嘉宾名单
guest=['Andy','Tiffany','Betty','Chris']
for i in guest:
    print('Hi , '+i+' , I invite you.')
print(guest[0]+" can't come.")
#3.5修改嘉宾名单
guest[0]='Jack'
print(guest)
for i in guest:
    print('Hi , '+i+' , I invite you.')
#3.6添加嘉宾
print('I find a big table!')
#使用insert插入元素到开头
guest.insert(0, 'Hulk')
#使用insert插入到列表中间
guest.insert(3,'Peter')
#使用append添加元素
guest.append('Fiona')
print(guest)
for i in guest:
    print('Hi , '+i+' , I invite you.')
#3.7缩减名单
print('I can only invite 2 persons.')
print(guest)
 #使用pop删除元素
print('Sorry for I can not invite you , '+guest.pop())
print('Sorry for I can not invite you , '+guest.pop())
print('Sorry for I can not invite you , '+guest.pop())
print('Sorry for I can not invite you , '+guest.pop())
print('Sorry for I can not invite you , '+guest.pop())
#邀请剩余人员
for i in guest:
    print('Hi , '+i+' , I also invite you.')
#清空列表
del guest[0:]
print(guest)

