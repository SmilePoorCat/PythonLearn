#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os

rootdir = 'I:\data'
paths = os.listdir(rootdir)
file = open('Chinese.txt','wb+')
list = []
for i in paths:
    f = open(os.path.join(rootdir,i),'rb')
    list.extend(f.readlines())
    print('已加载'+f.name)
    f.close()
list = set(list)
i = 0
#print(list.pop())
for s in list:

    file.write(s)
    i = i+1
    print('已写入:',str(i),'行，剩余：',str(len(list)-i))

file.close()
