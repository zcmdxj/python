#!/usr/bin/python3

##生成一个六位的数字
import random
dir (random)
for i in range(6):
	print (random.randint(0,9),end = "")

##随机生成1-100内的偶数
print (random.randrange(0,101,2))

##生成一个六位的数字和字母，其中第一位，第三位，第六位是随机字母
for i in range(6):
	if i%2 == 0:
		print (chr(random.randint(65,90)),end = "")
	else:
		print (i,end = "")

##生成0-4位随机数字和字母的组合
for i in range(4):
	ran_count = random.randint(0,3)
	if i == ran_count:
		print (chr(random.randint(65,90)),end = "")
	else:
		print (i,end = "") 

for i in range(4):
	rand_count = random.randint(0,3)
	if i == rand_count:
		print (chr(random.randint(65,90)),end = "")
	else:
		print (random.randint(0,9),end = "")


check_code = ''
for i in range(4):
	rand_count = random.randint(0,3)
	if i == rand_count:
		rand_count = chr(random.randint(65,90))
	check_code += str(rand_count)
	print (check_code)
