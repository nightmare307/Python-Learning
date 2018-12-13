# -*- coding: utf-8 -*
# 第三章练习1——失败
#求10的因数
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


# 第三章练习2
text='中国+china2017是-*/OK 很难a也不难'
#定义统计变量
letterL=letter=word=nums=syms=0
#定义循环初始循环变量
i=0
#定义字符串长度变量（感觉可以不用定义）
slen=len(text)
#定义当循环变量小于长度时进行循环
while i < len(text):
    if (ord(text[i])>127):
        word+=1
    elif (ord(text[i]) > 96 and ord(text[i]) < 123):
        letter+=1
    elif (ord(text[i]) > 64 and ord(text[i]) < 91):
        letterL += 1
    elif (ord(text[i])>31 and ord(text[i]) < 48):
        syms+=1
    else:
        nums+=1
    i+=1
print("语句中包含小写字母%d个,大写字母%d个,文字%d个,数字%d个,符号%d个"%(letter,letterL,word,nums,syms))
