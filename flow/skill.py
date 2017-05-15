#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/15 18:31
# @Author  : dk05408
# @Site    : 
# @File    : skill.py
# @Software: PyCharm

#原地交换两个数字

x,y = 10,20
print(x,y)

x,y = y,x
print(x,y)

#链状比较操作符
n = 10
result = 1<n<20
print(result)

result = 1>n<=9
print(result)


def small(a, b, c):
    return a if a <= b and a <= c else (b if b <= a and b <= c else c)


print(small(1, 0, 1))
print(small(1, 2, 2))
print(small(2, 2, 3))
print(small(5, 4, 3))

[m**2 if m > 10 else m**4 for m in range(50)]

multiStr = """select * from multi_row
where row_id < 5"""
print(multiStr)


multiStr= ("select * from multi_row "
"where row_id < 5 "
"order by age")
print(multiStr)

testList = [1, 2, 3]
x, y, z = testList

print(x, y, z)

# -> 1 2 3

import threading
import socket

print(threading)
print(socket)

testDict = {i: i * i for i in range(10)}
testSet = {i * 2 for i in range(10)}

print(testSet)
print(testDict)

import pdb
# pdb.set_trace()


test = [1, 3, 5, 7]
# print( dir(test) )


class Shapes:
    Circle, Square, Triangle, Quadrangle = range(4)


print(Shapes.Circle)
print(Shapes.Square)
print(Shapes.Triangle)
print(Shapes.Quadrangle)










