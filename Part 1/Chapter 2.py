# -*- coding: utf-8 -*
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
#字符串控制长度
