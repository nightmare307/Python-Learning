# -*- coding: utf-8 -*
from Modules_Part1 import * 
'''
def find_factor(nums):
    i=1
    str1=''
    print('%d????:'%(nums))
    while i<=nums:
        if nums%i==0:
            str1=str1+' '+str(i)
        i+=1
    print(str1)


num2_L=[10,15,20,35]
i=0
num_len=len(num2_L)
while i<num_len:
    find_factor(num2_L[i])
    i+=1
'''

from Modules_Part1 import find_factor
print(find_factor(20))


#主程序，对三酷猫钓鱼记账内容进行统计
d_date1 = {'鲫鱼': [17, 10.5], '鲤鱼': [8, 6.2], '鲢鱼': [7, 4.7]}  # 1月1日钓鱼记录
d_date2 = {'草鱼': [2, 7.2], '鲫鱼': [3, 12], '黑鱼': [6, 15]}  # 1月2日钓鱼记录
d_date3 = {'乌龟': [1, 78.10], '鲫鱼': [1, 10.78], '草鱼': [5, 7.92]}  # 1月3日钓鱼记录
fish_records = {'1月1日': d_date1, '1月2日': d_date2, '1月3日': d_date3}  # 所有钓鱼记录
#======================================天统计
print('===鱼每日统计====================')
for day, day_record in fish_records.items():
    day_stat(day, day_record)
#======================================
print('\n===鱼所有数量统计================')

name1 = ''
maxstat = ['', 0, '', 0, 0, 0]  # 前4个元素记录最大值，后2个记录总数量、总金额
# 对每种鱼的数量、金额,总数量、总金额、最大数量、最大金额进行统计
all_stat = allday_stat(fish_records, maxstat)
for name1, subs in all_stat.items():  # 打印所有鱼的统计
    print('%s 数量%d 金额 %.2f' % (name1, subs[0], subs[1]))

#===========================================
print('\n===最大值，总数量，总金额统计打印===')
PrintMaxValues(maxstat)
