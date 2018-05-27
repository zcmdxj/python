#!/usr/bin/python3
'''
0001 题：作为Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠卷），使用Python 如何生成200 个激活码或者优惠卷。
'''

import string
import random

'''
这个函数用来创造一个随机的字符串
'''
def coupon_creator(digit):
    coupon = ''
    for word in range(digit):
        coupon += random.choice(string.ascii_uppercase + string.digits)
    return coupon
'''
这个函数用来定义所生成优惠卷的个数
'''
def two_hundred_coupons():
    data = ''
    count = 1
    for count in range(200):
        digit = 12 
        count += 1
       '''
       三种字符串拼接的方式
       (1)使用+ 号进行字符串拼接
      （2）使用% 占位进行拼接
      （3）使用format 格式化输出拼接
      '''
#        data += 'coupon on.'+str(count)+' '+coupon_creator(digit)+'\n'
#        data += "coupon on.%s %s\n"%(str(count),coupon_creator(digit))
        data += "coupon on.{} {}\n".format(str(count),coupon_creator(digit))
    return data

if __name__ == '__main__':
    coupondata = open('coupondata.txt','w')
    coupondata.write(two_hundred_coupons())
    coupondata.close()
