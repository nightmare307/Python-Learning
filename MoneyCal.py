# -*- coding: utf-8 -*

import datetime
import calendar
import time
from dateutil.relativedelta import relativedelta

#等额本金计算器
print('--------'*7+'等额本金还款计算器'+'--------'*7)
#定义初始期数变量
i = 1
#定义期数变量
terms=int(input('请输入借款期数：'))
#定义本金 
#capital = 50000
capital = float(input('请输入借款金额：'))
#定义日利率
#dayrate= 0.0004
dayrate=float(input('请输入借款日利率：'))
#定义剩余本金
recapital = 0
#定义每月应还本金
#monthcapital=capital/20
monthcapital =capital/terms
#定义借款日期
#datefirst = datetime.date(2018, 11, 13)
firsta =input('请输入借款日期（yyyy-mm-dd）：')
firstt = time.strptime(firsta, "%Y-%m-%d")
fy,fm, fd = firstt[0:3]
datefirst = datetime.datetime(fy, fm, fd).date()
#定义第一期还款日
#datefirstback = datetime.date(2018, 12, 24)
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
#定义总利息列表
z=[]
print('--------'*7+'还款计划'+'--------'*7)
print('共%d期，日利率%.2f%%，月利率%.3f%%，年利率%.3f%%' %  (terms, dayrate*100, dayrate*30*100, dayrate*365*100))
while i <=terms:
       if i==1:
           recapital = capital
           dayuse = (datefirstback-datefirst).days
           interest = recapital*dayrate*dayuse
           monthall = monthcapital+interest
           print('第%d期，剩余待还本金%d，还款本金%.2f元，当期利息%.2f元，还款本息合计%.2f元，还款日为%s，使用天数%d天'%(i,recapital,monthcapital,interest,monthall,datefirstback,dayuse))
           z.insert(0,float('% .3f' % (interest)))
       else:
           recapital = (capital-monthcapital*(i-1))
           dateback = datefirstback+relativedelta(months=i-1)
           datebacka = datefirstback+relativedelta(months=i-2)
           dayuse = (dateback-datebacka).days
           interest = recapital*dayrate*dayuse
           monthall = monthcapital+interest

           #print(dateback)
           #print(datebacka)
           print('第%d期，剩余待还本金%d，还款本金%.2f元，当期利息%.2f元，还款本息合计%.2f元，还款日为%s，使用天数%d天' % (i, recapital, monthcapital, interest, monthall, dateback, dayuse))
           z.append(float('% .3f' % (interest)))
       i+=1
print(z)
total=sum(z)
print(total)
