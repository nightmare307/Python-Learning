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
records = [zhang,ding,mao,wang,li]
total = 0
everytotal = []
i=0
z=0
for nrecords in records:
    everytotal.append(nrecords[1][1]*nrecords[1][2]+nrecords[2][1]*nrecords[2][2]+nrecords[3][1]*nrecords[3][2])
    while z<len(everytotal):
        print('%s同学投资%.2f元'%(nrecords[0],everytotal[z]))
        z+=1
total = sum(everytotal)
print('编程兴趣小组总投入%.2f元'%(total))
