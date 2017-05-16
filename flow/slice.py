#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/5/16 15:57
# @Author  : dk05408
# @Site    : 
# @File    : slice.py
# @Software: PyCharm

colors = ["red", "blue", "green"]
print(colors[-1])  #green
print(colors[-3])  #red

li = ["A","B","C","D","E"]
print(li[0:3]) #['A', 'B', 'C']
print(li[2: ]) #['C', 'D', 'E']
print(li[1:3]) #['B', 'C']
print(li[0::2]) #['A', 'C', 'E']
print(li[::2]) #['A', 'C', 'E']
print(li[:])  #['A', 'B', 'C', 'D', 'E']

#-5 -4 -3  -2 -1
# A  B  C  D  E
# 0  1  2  3  4

print(li[0:-4]) #['A']
print(li[-4:-2]) #['B', 'C']
print(li[-2:-4]) #[]
print(li[-4:2]) #['B']

print(li[-1:-3:-1]) #['E', 'D']
print(li[-1:1:-1]) #['E', 'D', 'C']
print(li[3:1:-1]) #['D', 'C']
print(li[3:-3:-1]) #['D']

print(li[-1:-3]) #[]
print(li[-1:1]) #[]
print(li[3:1]) #[]
print(li[3:-3]) #[]

print(li[::-1]) #['E', 'D', 'C', 'B', 'A']
print(li[:]) #['A', 'B', 'C', 'D', 'E']

print(li[-100:100]) #['A', 'B', 'C', 'D', 'E'] li[0:5]
print(li[-100:-200]) #[] li[0:0]
print(li[100:200]) #[] li[5:5]
print(li[0:100])  #['A', 'B', 'C', 'D', 'E']
print(li[0:])  #['A', 'B', 'C', 'D', 'E']
print(li[0:5:3]) #['A', 'D']

str ="01234567890123456789"
print(str[0::5])


print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
def between(beg, end, mid):
    # 判断mid是否位于begin和end之间
    return end > mid >= beg or end < mid <= beg


def get_slice(a, beg, end, delta=1):
    # 数组切片get方式
    if delta == 0: raise ValueError("slice step cannot be 0")
    # 将负数下标转化一下
    if beg < 0: beg += len(a)
    if end < 0: end += len(a)
    # 如果转化完成之后依然不在合法范围内，则返回空列表
    if beg < 0 and end < 0 or beg >= len(a) and end >= len(a): return []
    # 如果方向不同，则返回空列表
    if (end - beg) * delta <= 0: return []
    # 将越界的部分进行裁剪
    beg = max(0, min(beg, len(a) - 1))
    end = max(-1, min(end, len(a)))
    ans = []
    i = beg
    while between(beg, end, i):
        ans.append(a[i])
        i += delta
    return ans


def set_slice(a, li, beg, end, delta=1):
    if delta == 0: raise ValueError("slice step cannot be 0")
    if delta == 1:
        # 如果delta==1，那么li的长度可以随意
        if beg < 0: beg += len(a)
        if end < 0: end += len(a)
        beg = max(0, min(beg, len(a) - 1))
        end = max(-1, min(end, len(a)))
        for i in range(beg, end):
            del a[beg]
        for i in reversed(li):
            a.insert(beg, i)
    else:
        # delta!=1,相当于替换
        if len(get_slice(a, beg, end, delta)) != len(li): raise ValueError("array don't match")
        if len(li) == 0: return
        if beg < 0: beg += len(a)
        if end < 0: end += len(a)
        beg = max(0, min(beg, len(a) - 1))
        # 用li中的全部元素逐一替换
        for ind, value in enumerate(li):
            a[ind * delta + beg] = value


def test_getSlice():
    a = list(range(10))
    import random
    for i in range(10):
        beg = random.randint(-15, 15)
        end = random.randint(-15, 15)
        delta = 0
        while delta == 0: delta = random.randint(-15, 15)
        print(len(get_slice(a, beg, end, delta)) == len(a[beg:end:delta]), beg, end, delta)


def test_setSlice():
    import random
    for i in range(10):
        a = list(range(10))
        print("a", a)
        beg = random.randint(-15, 15)
        end = random.randint(-15, 15)
        print('beg,end',beg,end)
        delta = 0
        while delta == 0: delta = random.randint(-5, 5)
        sz = len(a[beg:end:delta])
        if delta == 1: sz = random.randint(0, 4)
        li = [random.randint(0, 100) for i in range(sz)]
        set_slice(a, li, beg, end, delta)
        mine = a
        a = list(range(10))
        a[beg:end:delta] = li
        print("a",a)
        print("mine", mine)
        print(a == mine)


test_setSlice()

rna =range(10);
print(rna)
print(list(rna))
print(between(0,1,1))
print(between(0,10,1))