#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019年12月29日 
# @Author  : ghost-guest
# @Site    : 
# @File    : test.py
# @Software: PyCharm
# 说明： 

from random import sample
from os import listdir
import os
# a = range(1000)
# print(a)
# b = sample(a, 5)
# print(b)
# dir_l = listdir('/Users/mac/Desktop/python')
# fns = [fn for fn in dir_l if fn.endswith('.xlsx')]
# print(fns)


# 获取某个目录下的所有的execl的文件的路径，包括层级目录
f_list = []
for root, dirs, files in os.walk('/Users/mac/Desktop/python'):
    for file in files:
        f = os.path.join(root, file)
        if f.endswith('.xlsx'):
            f_list.append(f)
print(f_list)
print("aaaaaaaaaa")
