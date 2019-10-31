# -*- coding: utf-8 -*
def display_message():
    '''显示信息'''
    print('This chapter we learn about function')

#*8.2喜欢的图书
def favourite_book(book):
    '''显示信息'''
    print('One of my favorite books is %s' % (book))

#*8.3T恤
def make_shirt(size, word):
    '''打印衣服尺码及文字'''
    print('Your T-shirt size is %s , the word is %s' % (size, word))

#*8.4大号T恤
def make_shirt_default_word(size, word='I Love Python'):
    '''有文字默认值的函数'''
    print('Your T-shirt size is %s , the word is %s' % (size, word))

#*8.5城市
def describe_city(city, country='China'):
    '''城市及所属国家'''
    print('%s is in %s' % (city, country))

#*8.6城市名
def city_country(city, country):
    '''城市及国家'''
    full = city + ',' + country
    return full.title()

#*8.7专辑 8.8自己的专辑
def make_album(name, album_name, album_year='',):
    '''定义歌手信息'''
    if album_year:
        album = {'singer': name, 'album': album_name, }
    else:
        album = {'singer': name, 'album': album_name, 'year': album_year, }
    return album

#*8.9魔术师
def magician(names):
    '''展示魔术师'''
    for name in names:
        print('Here is The magician %s' % (name.title()))
    return

#*8.10了不起的魔术师
def make_great(magics, greatmagics):
    '''魔术师增加前缀'''
    for magic in magics:
        magic = 'the great '+magic.title()
        greatmagics.append(magic)
    print(greatmagics)
    return