#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/15 18:31
# @Author  : dk05408
# @Site    : 
# @File    : skill.py
# @Software: PyCharm

#原地交换两个数字
import math

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


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10)]


print(sorted(student_objects, key=lambda student: student.age))

from operator import attrgetter
print(sorted(student_objects, key=attrgetter('age')))
#[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

print(sorted(student_objects, key=attrgetter('grade', 'age')))
#[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]

def displayNumType(num):
    print(num,'is')
    if isinstance(num,(int,float,complex)):
        print('a number of type:',type(num).__name__)
    else:
        print('not a number at all!!')

displayNumType(-69)
displayNumType(-692.3)
displayNumType(3+3j)
displayNumType('11')

print(1/2)
print(1.0/2.0)
print(4//3)
print(4**2)
print(pow(4,2))
print(abs(-41))

print(math.pi)
print("int",int(math.pi))
print("round",round(math.pi))
print("floor",math.floor(math.pi))
for eachNum in range(10):
    print("eachNum = ",eachNum)
    print(round(math.pi, eachNum))




if __name__ =="__main__":
    print("first method")

