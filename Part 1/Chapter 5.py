# -*- coding: utf-8 -*
'''
#===========================钓鱼原始记录
d_date1 = {'鲫鱼': [18, 10.5], '鲤鱼': [8, 6.2], '鲢鱼': [7, 4.7]}  # 1月1日钓鱼记录
d_date2 = {'草鱼': [2, 7.2], '鲫鱼': [3, 12], '黑鱼': [6, 15]}  # 1月2日钓鱼记录
d_date3 = {'乌龟': [1, 71], '鲫鱼': [1, 9.8],
           '草鱼': [5, 7.2], '黄鱼': [2, 40]}  # 1月3日钓鱼记录
fish_records = {'1月1日': d_date1, '1月2日': d_date2, '1月3日': d_date3}  # 所有钓鱼记录
#===========================修改错误的纪录
d_date1['鲫鱼'] = [17, 10.5]  # 修改键"鲫鱼"对应的值
del(d_date3['黄鱼'])  # 删除键"黄鱼"指定的元素
for get_name, get_L in d_date3.items():  # '1月3日'所有的单价都上浮10%
    get_L[1] = get_L[1]*1.1  # 把列表对应的单价乘以1.1,并修改列表单价
    d_date3[get_name] = get_L  # 修改字典变量对应的值
#===========================打印修改后的结果
nums = 0  # 钓鱼总数量初始化定义
amount = 0  # 钓鱼总金额初始化定义
day = ''  # 日期记录变量初始化定义
day_record = {}  # 钓鱼每天记录字典变量初始化定义
for day, day_record in fish_records.items():  # 循环获取每天记录(元组形式)
    print('%s钓鱼记录为:' % (day))  # 打印当天的日期
    for name, sub_recods in day_record.items():  # 循环获取当天鱼与数量,单价关系的记录
        nums += sub_recods[0]  # 数量累加
        amount += sub_recods[0]*sub_recods[1]  # 金额累加
        print('    %s数量%d,单价%.2f元' %
              (name, sub_recods[0], sub_recods[1]))  # 打印名称,数量,单价
print('钓鱼总数量为%d,总金额为%.2f元' % (nums, amount))  # 打印总数量,总金额
#打印fish_records d_date1 d_date3
#删除了黄鱼 鲫鱼改为了17
print(fish_records)
print(d_date1)
print(d_date3)
'''


#期末考试成绩管理
#定义人员和成绩列表对应的字典
results={'小明':[95.5,98,97],'小王':[96,92,82],'小丽':[91,100,90],'小花':[88,93,99]}
names = ['小明','小王','小丽','小花']
print(results)
#for name,ch in result.items():
print(results['小明'][0])
#names=''
ch=0
chsum=0
en=0
ensum=0
ma=0
masum=0
maxscore={'语文':['',0],'英语':['',0],'数学':['',0]}
for names in results:
    ch=results[names][0]
    chsum+=ch
    en = results[names][1]
    ensum += en
    ma = results[names][2]
    masum += ma
print('语文总分%.1f，英语总分%.1f，数学总分%.1f' % (chsum,ensum,masum))
print('语文平均分%.2f，英语平均分%.2f，数学平均分%.2f' %
      (chsum/len(names), ensum/len(names), masum/len(names)))

for name,score in results.items():
      if maxscore['语文'][1]<score[0]:
          maxscore['语文']=[name,score[0]]
      elif maxscore['英语'][1] < score[1]:
          maxscore['英语']=[name, score[1]]
      elif maxscore['数学'][1] < score[2]:
          maxscore['数学']=[name, score[2]]
print(maxscore)
