# -*- coding: utf-8 -*
#*8.1消息
#!无形参版本
def display_message():
    '''显示信息'''
    print('This chapter we learn about function')
display_message()

#*8.2喜欢的图书
def favourite_book(book):
    '''显示信息'''
    print('One of my favorite books is %s' % (book))
favourite_book('Kill Bill')

#*8.3T恤
def make_shirt(size,word):
    '''打印衣服尺码及文字'''
    print('Your T-shirt size is %s , the word is %s'%(size,word))
make_shirt('M','Kill Bill')

#*8.4大号T恤
def make_shirt_default_word(size,word='I Love Python'):
    '''有文字默认值的函数'''
    print('Your T-shirt size is %s , the word is %s' % (size, word))
make_shirt_default_word('L')
make_shirt_default_word('M')
make_shirt_default_word('SS','Kill Bill')

#*8.5城市
def describe_city(city,country='China'):
    '''城市及所属国家'''
    print('%s is in %s'%(city,country))
describe_city('Beijing')
describe_city('HeBei')
describe_city('London','Britain')

#*8.6城市名
def city_country(city,country):
    '''城市及国家'''
    full=city + ',' + country
    return full.title()
while True:
    print("\n Please input city :\nenter 'q' to quit.")
    c=input('City:')
    if c=='q':
        break
    na=input('Country:')
    if na=='q':
        break
    cna=city_country(c,na)
    print(cna)


