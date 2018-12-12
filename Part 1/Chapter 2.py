# -*- coding: utf-8 -*
# 引入时间模块
import time
# 2.1变量
a = 5
print(a)
one, two, three = 'Great', 'Good', 'Well'
print(one, two, three)
one = two = three = 1000
print(one, two, three)

# 2.2字符串
name = 'Tom'
name1 = "Jerry"
name2 = '''Sreck'''
print(name, name1, name2)
name3, name4, name5 = 'Tom', "Jerry", '''Srec'''
print(name3, name5, name4)

# 2.2.1 字符串操作
grammar = 'I am the King of the World!'
# 读取下标为5的字符
print(grammar[5])
# 读取下标2-13 左开右闭区间
print(grammar[2:13])
# 读取下标0-13 左开右闭
print(grammar[:13])
# 读取整个串
print(grammar[:])
# 步长为3读取
print(grammar[::3])
# 倒序读取
print(grammar[-13:-1])
# 字符串合并
job = 'Hoster'
record = name + ',' + job
print(record)
# 字符串替换
new_grammar=grammar[:21]+'Hell'
print(new_grammar)

#2.2.2其他常用操作
#获取字符串长度
len (grammar)

#第二章练习
0b11^0b00
bin(3)

#第二章课后题
# 定义数量变量
num1, num2, num3 = 5, 6, 9
# 定义价格变量
price1, price2, price3 = 8.1, 8.2, 8
# 定义鱼品种变量
fish1, fish2, fish3 = '鲫鱼', '鲤鱼', '草鱼'
# 定义日期字符串
date = '2017年12月'
Total_Num = num1+num2+num3  # 总的鱼数
Total_Amount = num1*price1+num2*price2+num3*price3  # 总金额
print("-----"*4+"三酷猫记账单"+"-----"*4)
print('钓鱼地点   '+'钓鱼日期   '+'   鱼名  '+'数量（条）'+' 单价（元）')
print('左小河    '+date+'1日 '+fish1+'  '+str(num1)+'         '+str(price1))
print('右小河    '+date+'2日 '+fish2+'  '+str(num2)+'         '+str(price2))
print('长  江    '+date+'3日 '+fish3+'  '+str(num3)+'         '+str(price3))
print("----"*12+'--')
# 计算合计 数量格式化为整数 价格格式化为字符串浮点2位小数
print('鱼数总计%d条，市场价格总计%.2f元，每天平均钓鱼数量约%d条(%f条)'
      % (Total_Num, Total_Amount, int(Total_Num/3), Total_Num/3))
# 鱼价格总平均值
Ave_price_all = Total_Amount / Total_Num
print('平均价格约%d元，平均价格较精确%.2f元，平均价格实际%f元'
      % (Total_Num, Total_Amount, Ave_price_all))
#增加记账日期及人名
localtime = time.asctime(time.localtime(time.time()))
print("----"*12+'--')
print('记账日期：', localtime,"\n记账人：Chris")
