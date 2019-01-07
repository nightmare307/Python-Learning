
# -*- coding: utf-8 -*
# 带参数nums的求因数的自定义函数
def find_factor(nums):  
    #用一对三个单引号来包括描述文档
    '''
    find_factor是自定义函数
    nums是传递一个正整数的参数
    以字符串形式返回一个正整数的所有因数
    '''
    # 不是整型，提示出错，并终止函数执行
    if type(nums) != int:
        # 提示传递值类型出错
        print('输入值类型出错,必须是整数!')
        # 终止函数执行
        return 
    # 小于等于0的整数不在求因数范围之内
    if nums <= 0:
        # 提示传输值范围出错
        print('输入值范围出错,必须正整数!')  
        # 终止函数执行
        return  
    i = 1
    str1 = ''
    # 循环求nums传入值的因数
    while i <= nums:  
        # 求传入值的因数
        if nums % i == 0:  
            str1 = str1+' '+str(i)
        i += 1
    # 返回因数
    return str1  

#统计鱼自定义模块


def day_stat(day, fishs):  # 统计每天的鱼，并保存到统计字典里
    '''统计每天的鱼，并保存到统计字典里
       day为字符串参数
       fishs为两层嵌套字典参数'''
    nums = 0  # 数量
    amount = 0  # 金额
    for name0, sub_records in fishs.items():
        print('%s数量%d单价%.2f元' % (name0, sub_records[0], sub_records[1]))
        nums += sub_records[0]
        amount += sub_records[0]*sub_records[1]
    print('%s数量小计%d金额小计%.2f' % (day, nums, amount))


def allday_stat(fishs, maxs):  # 统计所有鱼，并保存到统计字典里
    '''统计所有鱼，并保存到统计字典里
       fishs为两层嵌套字典参数'''
    name1 = ""
    sub_recods = {}
    stat_record = {}
    for day, day_record in fishs.items():  # 循环获取每天记录(元组形式)
        for name1, sub_recods in day_record.items():  # 循环获取当天鱼与数量,单价关系的记录
            if name1 in stat_record:  # 判断鱼是否在统计字典里,在,则做累计处理
                stat_record[name1][0] += sub_recods[0]  # 每种鱼数量累计
                stat_record[name1][1] += sub_recods[0]*sub_recods[1]  # 每种鱼金额累计
            else:
                stat_record[name1] = [sub_recods[0], sub_recods[0]
                                      * sub_recods[1]]  # 第一次累计,直接在字典里赋值
    #====================================================
    for name1, nums in stat_record.items():
        if maxs[1] < nums[0]:  # 求最大数量
            maxs[0] = name1
            maxs[1] = nums[0]
        if maxs[3] < nums[1]:  # 求最大金额
            maxs[2] = name1
            maxs[3] = nums[1]
        maxs[4] = maxs[4]+nums[0]  # 求所有数量
        maxs[5] = maxs[5]+nums[1]  # 求累计总金额
    #考虑一下:maxs值是怎么返回到主程序的代码里的?
    return stat_record


def PrintMaxValues(maxstat1):  # 打印最大值
    '''打印最大值
       maxstat1[:4]为列表参数，记录最大值
       maxstat1[4]记录总数量
       maxstat1[5]记录总金额'''
    print('最大数量的鱼是%s,%d条' % (maxstat1[0], maxstat1[1]))
    print('最大金额的鱼是%s,%.2f元' % (maxstat1[2], maxstat1[3]))
    print('钓鱼总数量为%d,总金额为%.2f元' % (maxstat1[4], maxstat1[5]))  # 打印总数量,总金额



