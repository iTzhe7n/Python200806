# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 09:42:04 2020

@author: user
"""

file = open('123.jpg','rb')
img =file.read()
file.close()

file = open('複製.jpg','wb')
file.write(img)
file.close()
