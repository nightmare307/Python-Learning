# -*- coding: utf-8 -*
def find_factor(nums):
    i=1
    str1=''
    print('%d的因数是:'%(nums))
    while i<=nums:
        if nums%i==0:
            str1=str1+' '+str(i)
        i+=1
    print(str1)


num2_L=[10,15,20,35]
i=0
num_len=len(num2_L)
while i<num_len:
    find_factor(num2_L[i])
    i+=1
