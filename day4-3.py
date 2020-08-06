# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 10:03:37 2020

@author: user
"""
import os.path
d={}

def c():
    print('-----------------')
    print('1.建立成績')
    print('2.列出所有成績')
    print('3.成績查詢系統')
    print('4.離開系統')
print("#############################")
print("#歡迎進入成績系統#")
print("#############################")

if not os.path.isfile('mylist.txt'):
    fo = open('mylist.txt','w')
    print("新檔案")
else:
    fo = open('mylist.txt','r')
    print('舊檔案')
'''
for row in fo.readlinrd():
    data = row.split(':')
    
    key = data[0]
    value = data[1] 
    #value = value.strip()
   
    d[key]=value
fo.close()            
print(d)

'''

while True:
    c() #call function
    m = input('請輸入指令: ')
    
    if m == '1' :
        while True:
            b = input('請輸入名子(0跳出):')
            if b == '0':
                break
            if b not in d:
                v = input('請輸入成績:')
                d[b]=v
            else:
                print('已存入')
        print(d)
    
        fo = open('mylist.txt','w')
        for key,value in d.items():
            fo.write(key)
            fo.write(':')
            fo.write(value)
            fo.write('\n')