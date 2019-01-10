# -*- coding: utf-8 -*
#4.1食物
foods=['Humburg','Pizza','Cheese','Steak']
for food in foods:
    print('I like '+food+' !')
print('I really love foods')
#4.2动物
animals=['dog','cat','fish']
for animal in animals:
    print(animal)
    print(animal.title()+' would make a great pet. \n')
print('Any of these animals would make a great pet!\n')

#4.3数到20
twenty=[num for num in range(1,21)]
print(twenty)
#4.4一百万
million=[mega for mega in range(1,1000001)]
#4.5计算一百万
#print(million)
print(min(million))
print(max(million))
print(sum(million))
#4.6奇数
odds=[odd for odd in range(1,21,2)]
print(odds)
#4.7 3的倍数
triples=[]
for triple in range(3,31):
    if triple%3==0:
        triples.append(triple)
print(triples)
#4.8立方
Cubes=[]
for Cube in range(1,11):
    Cubes.append(Cube**3)
print(Cubes)
#4.9立方解析
cubes=[cube**3 for cube in range(1,11)]
print(cubes)
