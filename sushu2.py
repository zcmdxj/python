#!/usr/bin/python3

for i in range(2,21):
    temp = 0
    for j in range(2,i):
        if i%j == 0:
            break
        else:
            temp = 1
    if temp == 1:
        print (i)

 
