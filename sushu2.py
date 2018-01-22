#!/usr/bin/python3


##打印１－２０范围内的素数，共３个版本
#version1
for i in range(2,21):
    temp = 0
    for j in range(2,i):
        if i%j == 0:
            break
        else:
            temp = 1
    if temp == 1:
        print (i)


#version2
for i in range(2,21):
    temp = 0
    x = int(i/2)
    for j in range(2,x+1):
        if i%x == 0:
            break
        else:
            temp = 1
    if temp == 1:
        print(i)


#version3
import math
for i in range(2,21):
    temp = 0
    x = int(math.sqrt(i))
    for j in (2,x+1):
        if i%j == 0:
            break
        else:
            temp = 1
    if temp == 1:
        print(i)
