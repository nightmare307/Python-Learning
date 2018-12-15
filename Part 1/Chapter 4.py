# -*- coding: utf-8 -*
# 尝试使用列表index更改数据
list=['鲶鱼',18,'黑鱼',20]
cate=list.index('黑鱼')
print(list[list.index('黑鱼')+1]*1.5)


#第四章实验1
#定义列表和元组
zhang = ['张力', ('笔记本电脑', 1, 5000), ('U盘', 1, 123), ('耳麦', 1, 500)]
ding = ['丁玲', ('笔记本电脑', 1, 5000), ('U盘', 1, 123), ('耳麦', 1, 100)]
mao = ['毛小', ('笔记本电脑', 1, 5000), ('U盘', 1, 123), ('耳麦', 1, 88)]
wang = ['王刚', ('笔记本电脑', 1, 5000), ('U盘', 1, 123), ('耳麦', 1, 200)]
li = ['李云', ('笔记本电脑', 1, 5000), ('U盘', 1, 123), ('耳麦', 1, 100)]
#更改毛小名字为毛大
print(mao.index('毛小'))
mao[0] = '毛大'
print(mao)
#定义姓名列表
records = [zhang,ding,mao,wang,li]
#定义总金额变量
total = 0
#定义单人金额列表
everytotal = []
#定义姓名循环查找变量
z=0
#使用for循环查找数量和金额
for nrecords in records:
    #使用列表中元素查找的方式查找每人三类产品金额(列表中第二个元素的第二项乘以第三项，第三个元素的第二项乘以第三项，第四个元素的第二项乘以第三项)
    #使用查找出来的元素添加到新的列表中
    everytotal.append(nrecords[1][1]*nrecords[1][2]+nrecords[2][1]*nrecords[2][2]+nrecords[3][1]*nrecords[3][2])
    #使用while循环查找姓名，使用列表长度作为限制跳出值，将查询结果打印，并以两位精度小数点打印
    while z<len(everytotal):
        print('%s同学投资%.2f元'%(nrecords[0],everytotal[z]))
        z+=1
#使用sum函数求总金额并以小数点两位精度打印打印
total = sum(everytotal)
print('编程兴趣小组总投入%.2f元'%(total))
