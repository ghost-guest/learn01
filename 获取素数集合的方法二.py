#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019年12月28日 
# @Author  : ghost-guest
# @Site    : 
# @File    : 获取素数集合的方法二.py
# @Software: PyCharm
# 说明： 
maxNumber = int(input('请输入一个大于2的自然数：'))
lst = list(range(2, maxNumber))
# 最大整数的平方根
m = int(maxNumber**0.5)
print(m)
for index, value in enumerate(lst):
    # 如果当前的数字已经大于最大整数的平方根，结束判断
    if value > m:
        break
    # 使用切片对该位置之后的元素进行过滤和替换
    print(index)
    print(value)
    lst[index+1:] = filter(lambda x: x % value != 0, lst[index+1:])
    print(lst[index+1:])
print(lst)
