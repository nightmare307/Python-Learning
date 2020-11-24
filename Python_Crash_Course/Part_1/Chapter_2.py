# -*- coding: utf-8 -*
#2.1简单消息
print ("hello world")
#2.2多条简单消息
print("hello world")
print("hello Python world")
#2.3个性化消息 2.4调整名字大小写
name='    Chris   '
print('Hello '+name+' , would you like to learn some Python today?')
print('Hello '+name.upper()+' , would you like to learn some Python today?')
print('Hello '+name.lower()+' , would you like to learn some Python today?')
print('Hello  '+name.lower().strip()+' , would you like to learn some Python today?')
print('Hello '+name.lower().lstrip()+' , would you like to learn some Python today?')
print('Hello '+name.lower().rstrip()+' , would you like to learn some Python today?')
#2.5名言
print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')
#2.6名言2
famous_person='Chris Lee'
message = 'Albert Einstein once said, “A person who never made a mistake never tried anything new.”'
print(famous_person+' once said '+message)
#2.8 数字8
print(2*4)
print(16-8)
print(8.0/1)
print(4+4)
#2.9最喜欢的数字
favorite=4
print('My favorite number is '+str(favorite))
#2.10添加注释
#2.11Zen of Python
import this
zen = "".join([this.d.get(c, c) for c in this.s])
print(zen)