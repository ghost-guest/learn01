#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019年12月19日 
# @Author  : ghost-guest
# @Site    : 
# @File    : numpy_1.py
# @Software: PyCharm
# 说明： 
import numpy as np

# 创建数组
a = np.array([1, 2, 3])
print(a)
# 创建二维数组
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
# 通过zeros 元组表示三行三列 如下
c = np.zeros((3, 3))
print(c)
# 通过ones生成元素为1的数组
d = np.ones((3, 3))
print(d)
# 通过arange生成数组,生成的一维的数组
e = np.arange(1, 9, 2)
print(e)
# 通过linspace生成一个等差数列
f = np.linspace(1, 8, 5)
print(f)
# logspace生成等比数列,默认底数为10，通过base设置底数
g = np.logspace(0, 2, 5, base=2)
print(g)
# 使用random创建随机数
h = np.random.random((3, 3))
print(h)
i = np.random.randint(1, 9, size=(3, 3))
print(i)
