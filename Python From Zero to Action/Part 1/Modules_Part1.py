
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
