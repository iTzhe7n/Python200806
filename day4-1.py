# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 09:05:03 2020

@author: user
"""
import os.path
if os.path.isfile('my.txt'):
    print('file存在')
else:
    print('file不存在')

fo = open('my.txt','w')
fo.write('hi')
fo = open('my.txt','r')
n = fo.read()
print(n)

fo = open('my.txt','a')
fo.write('.....')

fo = open('my.txt','a')
fo.write('OK')

fo = open('my.txt','a')
fo.write('.....')


fo = open('my.txt','a')
fo.write('.....')

fo.close()