# -*- coding: utf-8 -*

import datetime
import calendar
import time
from dateutil.relativedelta import relativedelta

#等额本金计算器
print('--------'*6+'还款计算器'+'--------'*7)

#定义还款方式
mode=input('请输入还款类型(等额本金/等额本息)：')
while mode == ''or mode != '等额本金' or mode != '等额本息':
    print('请输入正确的还款类型(等额本金/等额本息)：')
    mode = input('请输入还款类型(等额本金/等额本息)：')

#定义初始期数变量
i = 1
#定义期数变量
terms=int(input('请输入借款期数：'))
while terms <= 0:
    print('请输入大于零的正整数')
    terms = int(input('请输入借款期数：'))
#定义本金 
#capital = 50000
capital = float(input('请输入借款金额：'))
while capital <=0:
    print('请输入大于零的正数')
    capital = float(input('请输入借款金额：'))
#定义利率
#dayrate= 0.0004
dayrate=float(input('请输入借款日利率(百分比)：'))*0.01
monthrate = float(input('请输入借款月利率(百分比)：'))*0.01
yearrate = float(input('请输入借款年利率(百分比)：'))*0.01
#定义剩余本金
recapital = 0
#定义每月应还本金
#monthcapital=capital/20
monthcapital =capital/terms
#定义借款日期
#datefirst = datetime.date(2018, 11, 13)
firsta =input('请输入借款日期（yyyy-mm-dd），不填写默认为当日：')
if firsta == '':
    datefirst=datetime.datetime.now().date()
else:
    firstt = time.strptime(firsta, "%Y-%m-%d")
    fy,fm, fd = firstt[0:3]
    datefirst = datetime.datetime(fy, fm, fd).date()
#定义第一期还款日
#datefirstback = datetime.date(2018, 12, 24)
fbacka = input('请输入第一期还款日（yyyy-mm-dd）：')
#当输入值为空时提示并重新输入
while fbacka=='':
   print('首期还款日不可为空，请重新输入！')
   fbacka = input('请输入第一期还款日（yyyy-mm-dd）：')
#计算初次还款日
fbackt = time.strptime(fbacka, "%Y-%m-%d")
fby, fbm, fbd = fbackt[0:3]
datefirstback = datetime.datetime(fby, fbm, fbd).date()
#比较首期还款日是否小于借款日并提示重新输入
while datefirstback < datefirst:
   print('首期还款日不可早于借款日期，请重新输入！')
   fbacka = input('请输入第一期还款日（yyyy-mm-dd）：')
   fbackt = time.strptime(fbacka, "%Y-%m-%d")
   fby, fbm, fbd = fbackt[0:3]
   datefirstback = datetime.datetime(fby, fbm, fbd).date()
#定义使用天数
dayuse=0
#定义每月应还利息
interest = 0
#定义每月应还本息
monthall = 0
#定义还款本息总额
totalall=[]
#定义总利息列表
interestall = []
#定义求和列表
total = [[totalall], [interestall]]
#-----------------------------------------等额本金-----------------------------------
if mode=='等额本金':
    print('--------'*7+'还款计划'+'--------'*7)
    while i <=terms:
       if i==1:
           recapital = capital
           dayuse = (datefirstback-datefirst).days
           interest = recapital*dayrate*dayuse
           monthall = monthcapital+interest
           #将首期总金额插入第一位
           totalall.insert(0, float('% .3f' % (monthall)))
           #将首期利息插入第一位
           interestall.insert(0,float('% .3f' % (interest))) 
           print('第%d期，剩余待还本金%d，还款本金%.2f元，当期利息%.2f元，还款本息合计%.2f元，还款日为%s，使用天数%d天' % (
               i, recapital, monthcapital, interest, monthall, datefirstback, dayuse))

       else:
           recapital = (capital-monthcapital*(i-1))
           dateback = datefirstback+relativedelta(months=i-1)
           datebacka = datefirstback+relativedelta(months=i-2)
           dayuse = (dateback-datebacka).days
           interest = recapital*dayrate*dayuse
           monthall = monthcapital+interest
           #print(dateback)
           #print(datebacka)
           # 添加其他期总额
           totalall.append(float('% .3f' % (monthall)))  
           # 添加其他期利息
           interestall.append(float('% .3f' % (interest)))  
           print('第%d期，剩余待还本金%d，还款本金%.2f元，当期利息%.2f元，还款本息合计%.2f元，还款日为%s，使用天数%d天' % (i, recapital, monthcapital, interest, monthall, dateback, dayuse))

       i+=1

#-----------------------------------------等额本息（未完成）-----------------------------------
elif mode == '等额本息':
    print('还没做')
    '''
    print('--------'*7+'还款计划'+'--------'*7)
    while i <= terms:
       if i == 1:
           recapital = capital
           dayuse = (datefirstback-datefirst).days
           interest = recapital*dayrate*dayuse
           monthall = monthcapital+interest
           #将首期总金额插入第一位
           totalall.insert(0, float('% .3f' % (monthall)))
           #将首期利息插入第一位
           interestall.insert(0, float('% .3f' % (interest)))
           print('第%d期，剩余待还本金%d，还款本金%.2f元，当期利息%.2f元，还款本息合计%.2f元，还款日为%s，使用天数%d天' % (
               i, recapital, monthcapital, interest, monthall, datefirstback, dayuse))

       else:
           recapital = (capital-monthcapital*(i-1))
           dateback = datefirstback+relativedelta(months=i-1)
           datebacka = datefirstback+relativedelta(months=i-2)
           dayuse = (dateback-datebacka).days
           interest = recapital*dayrate*dayuse
           monthall = monthcapital+interest
           #print(dateback)
           #print(datebacka)
           # 添加其他期总额
           totalall.append(float('% .3f' % (monthall)))
           # 添加其他期利息
           interestall.append(float('% .3f' % (interest)))
           print('第%d期，剩余待还本金%d，还款本金%.2f元，当期利息%.2f元，还款本息合计%.2f元，还款日为%s，使用天数%d天' % (
               i, recapital, monthcapital, interest, monthall, dateback, dayuse))

       i += 1
'''
#本息求和
totalsum = sum(totalall)
#利息求和
totalint = sum(interestall)
print('--------'*7+'合    计'+'--------'*7)
print('共%d期，日利率%.2f%%，月利率%.3f%%，年利率（365天计算）%.3f%%,年利率（360天计算）%.3f%%'%
      (terms, dayrate*100, dayrate*30*100, dayrate*365*100,dayrate*360*100))
print('总计还款%.2f元，其中本金总计%.2f元，利息合计%.2f元'%(totalsum,capital,totalint))

