# -*- coding: utf-8 -*

import datetime
import calendar
import time
from dateutil.relativedelta import relativedelta

#显示当前时间
datetime_now = datetime.datetime.now()
#3个月后的时间
datetime_three_month_ago = datetime_now + relativedelta(months=3)
print (datetime_three_month_ago)

#定义本金 利率 月还本金
capital = 50000
recapital=0
rate=0.0004
monthcapital=2500
#定义借款日期
datefirst = datetime.date(2018, 11, 13)
#定义期数
i = 1
datefirstback = datetime.date(2018, 12, 23)
#定义每月还款日期
dayuse=(datefirstback-datefirst).days+1
#databacka = datefirstback+relativedelta(months=i-1)
interest = recapital*rate*dayuse
monthall = 0
recapital = (capital-monthcapital)*i
while i <=20 and i!=0:
       if i==1:
           recapital = capital
           interest = recapital*rate*dayuse
           monthall = monthcapital+interest
           print('当前为第%d期，剩余待还本金%d，还款本金%.2f元，当期利息%.2f元，还款本息合计%.2f元，还款日为%s，使用天数%d天'%(i,recapital,monthcapital,interest,monthall,datefirstback,dayuse))
       else:
           recapital = (capital-monthcapital*(i-1))
           dateback = datefirstback+relativedelta(months=i-1)
           datebacka = datefirstback+relativedelta(months=i-2)
           dayuse = (dateback-datebacka).days
           interest = recapital*rate*dayuse
           monthall = monthcapital+interest
           #print(dateback)
           #print(datebacka)
           print('当前为第%d期，剩余待还本金%d，还款本金%.2f元，当期利息%.2f元，还款本息合计%.2f元，还款日为%s，使用天数%d天' % (i, recapital, monthcapital, interest, monthall, dateback, dayuse))
       i+=1

