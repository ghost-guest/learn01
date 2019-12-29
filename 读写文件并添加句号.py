#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2019年12月29日 
# @Author  : ghost-guest
# @Site    : 
# @File    : 读写文件并添加句号.py
# @Software: PyCharm
# 说明：

'''
编写一个程序，读写文件，要求在文件的每一行的后面添加一个句号，要求行号以#开始，并且所有行的
#垂直对齐。
'''

file_name = "demo.txt"
with open('demo.txt', "r") as fb:
    lines = fb.readlines()
# 返回一个列表中的最长子字符串
maxlength = len(max(lines, key=len))
print(maxlength)
# Python rstrip() 删除 string 字符串末尾的指定字符（默认为空格）.
# Python ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。

lines = [line.rstrip().ljust(maxlength)+'#'+str(index)+'\n' for index, line in enumerate(lines)]
print(lines)
with open("demo_new.txt", "w+") as fb:
    fb.writelines(lines)



