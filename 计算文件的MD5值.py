#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019年12月29日 
# @Author  : ghost-guest
# @Site    : 
# @File    : 计算文件的MD5值.py
# @Software: PyCharm
# 说明： 要求输入一个文件名，然后输出该文件的MD5值，如果文件不存在
# 就进行相应的提示

import hashlib
import os.path
filename = input('请输入文件名（包含完成路径）：')
if os.path.isfile(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        print(hashlib.md5(data).hexdigest())
else:
    print('文件不存在。')

