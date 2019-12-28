#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019年12月28日 
# @Author  : ghost-guest
# @Site    : 
# @File    : 垃圾邮件的识别.py
# @Software: PyCharm
# 说明： 


def check(text, rate=0.2):
    characters = '[]*-\/'
    num = sum(map(lambda ch: text.count(ch), characters))
    print(num)
    if num / len(text) > rate:
        return '垃圾邮件'
    return '正常邮件'


# 测试
text = '我公[司[免费[开发票，微*信*号同-号'
print(check(text))
print(check(text, 0.5))
