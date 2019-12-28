#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019年12月28日 
# @Author  : ghost-guest
# @Site    : 
# @File    : 获取一个自然数所包含的素数.py
# @Software: PyCharm
# 说明： 
num = int(input('请输入一个自然数：'))
lst = list(range(2, num+1))
print(lst)
for i in range(2, num+1):
    for j in range(2, i+1):
        mid_num = int(i**0.5)
        if j > mid_num:
            break
        if i % j == 0:
            lst.remove(i)
print(lst)
