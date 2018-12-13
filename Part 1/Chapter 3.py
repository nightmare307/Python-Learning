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
letter=word=nums=syms=0
i=0
slen=len(text)
while i<slen:
    if (ord(text[i])>126):
        word+=1
    elif (65>=ord(text[i]) <= 90 and 97>=ord(text[i]) <= 122):
        letter+=1
    elif (33 >= ord(text[i]) <= 47 and 58 >= ord(text[i]) <= 64):
        syms+=1
    i+=1
print("语句中包含字母%d个,文字%d个,数字%d个,符号%d个"%(letter,word,nums,syms))