# 第三章练习1——失败
#定义因数变量i
i=1
#定义结果集
result=''
#定义求和 初始值为0
total=0
#当i小于等于10的时候
while i<=10:
    #如果10除以i的余数为0
    if 10%i==0:
        #结果集变为上一结果集加变量i的字符串
        result = result+str(i)+','
        #和为求和当前值加i
        total+=i
    #变量i加一 进行下一循环
    i+=1
print('10的因数有%s因数累加和是%d' %(result,total))