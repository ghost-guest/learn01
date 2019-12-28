#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019年12月28日 
# @Author  : ghost-guest
# @Site    : 
# @File    : 使用蒙特卡罗法计算圆周率.py
# @Software: PyCharm
# 说明：
from random import random

times = int(input('请输入拯飞镖次数：'))
hits = 0
for i in range(times):
    x = random()
    y = random()
    if x*x + y*y <= 1:
        hits += 1
print(4.0 * hits/times)
