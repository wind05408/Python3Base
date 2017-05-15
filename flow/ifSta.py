#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/15 18:19
# @Author  : dk05408
# @Site    : 
# @File    : ifSta.py
# @Software: PyCharm
print("===============================if elif=====================")
x = int(input("Please enter an integer:"))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print("More")

print("===============================for=====================")
words =['cats','Dogs','Windows']
for w in  words:
    print(w,len(w))

for w in words[:]:
    if len(w)>6:
        words.insert(0,w)


print(words)