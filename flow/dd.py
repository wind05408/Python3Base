#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/15 19:53
# @Author  : dk05408
# @Site    : 
# @File    : dd.py
# @Software: PyCharm
import os


ls = os.linesep

#get filename
while True:
    #需要添加的语句，并且需要缩进，后面的四条语句也需要缩进
    fname = input("please input file name:\n")
    if os.path.exists(fname):
        print ("ERROR: '%s' already exists" % fname)
    else:
        break
#get file content (text) Lines
all_list = []
#all = []
print("\nEnter lines ('.' by itself to quit).\n")

#loop until user terminates input
while True:
    entry = input('> ')
    if entry == '.':
        break
    else:
        all_list.append(entry)
#write lines to file with proper line-ending
fobj = open(fname,'w')
fobj.writelines(['%s%s' % (x,ls) for x in all_list])
fobj.close()
print ('DONE!')