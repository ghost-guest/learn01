#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019年12月23日 
# @Author  : ghost-guest
# @Site    : 
# @File    : numpy2.py
# @Software: PyCharm
# 说明： 
import numpy as np

arr = np.arange(9).reshape(3, 3)
print(arr)
# 基本操作
# 数组与标量的运算
# 每一个元素的加减乘除的操作
print(arr+2)
print(arr*2)
# 两个数组的操作+-*/
arr1 = np.array([[1, 2], [4, 5]])
arr2 = np.array([[1, 2], [4, 5]])
print(arr1+arr2)
print(arr1*arr2)
# 矩阵积
print('='*30)
arr3 = np.dot(arr1, arr2)
print(arr3)
# 索引和切片
arr = np.random.randint(1, 9, size=(2, 3, 3))
print(arr)
# 取下标
print('='*30)
print(arr[1, 2])

# 切片
print('-'*20)
print(arr[:, :,  1])
# 花式索引
print('=*'*30)
arr = np.random.randint(1, 9, size=(8, 4))
print(arr)
print('='*20)
print('='*20)
# 取第一行，第三行，第五行的数据
print(arr[[0, 3, 5]])
print(arr[[0, 3, 5], [0, 3, 2]])
print('---'*20)
# 创建一个索引器，获取第一行的第一个，第三个，第二个元素，第三行的第一个，第三个，第二个
print(arr[np.ix_([0, 3, 5], [0, 3, 2])])

print("---"*20)
b = arr > 3
print(b)







