# -*- coding: utf-8 -*
from Chapter_8_modules import *
#*8.1消息
#!无形参版本
display_message()

#*8.2喜欢的图书
favorite_book('Kill Bill')

#*8.3T恤
make_shirt('M','Kill Bill')

#*8.4大号T恤
make_shirt_default_word('L')
make_shirt_default_word('M')
make_shirt_default_word('SS','Kill Bill')

#*8.5城市
describe_city('Beijing')
describe_city('HeBei')
describe_city('London','Britain')

#*8.6城市名
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
magicians=['jack','chris','jane','tiffany']
magician(magicians.copy())

#*8.10了不起的魔术师
great = ['jack', 'chris', 'jane', 'tiffany']
newgreat=[]
make_great(great,newgreat)