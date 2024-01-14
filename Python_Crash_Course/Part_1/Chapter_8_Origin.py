# -*- coding: utf-8 -*
#*8.1消息
#!无形参版本
def display_message():
    '''显示信息'''
    print('This chapter we learn about function')
display_message()

#*8.2喜欢的图书
def favorite_book(book):
    '''显示信息'''
    print('One of my favorite books is %s' % (book))
favorite_book('Kill Bill')

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

#*8.7专辑 8.8自己的专辑
def make_album(name,album_name,album_year='',):
    '''定义歌手信息'''
    if album_year:
        album = {'singer':name,'album':album_name,}
    else:
        album = {'singer': name, 'album': album_name,'year': album_year,  }
    return album

while True:
    print("\nPlease input single name :\nenter 'q' to quit.")
    sname=input('Single name :')
    if sname=='q':
        break
    print("\nPlease input album name :\nenter 'q' to quit.")
    aname = input('Album name :')
    if aname=='q':
        break
    print("\nPlease input album year :\nif you don\'t know , press enter \nenter 'q' to quit.")
    ayear = input('Album year :')
    if ayear == 'q':
        break
    album_info=make_album(sname,aname,ayear)
print(album_info)

#*8.9魔术师
def magician(names):
    '''展示魔术师'''
    for name in names:
        print('Here is The magician %s'%(name.title()))
    return
magicians=['jack','chris','jane','tiffany']
magician(magicians.copy())

#*8.10了不起的魔术师
def make_great(magics,greatmagics):
    '''魔术师增加前缀'''
    for magic in magics:
        magic='the great '+magic.title()
        greatmagics.append(magic)
    print(greatmagics)
    return
great = ['jack', 'chris', 'jane', 'tiffany']
newgreat=[]
make_great(great,newgreat)