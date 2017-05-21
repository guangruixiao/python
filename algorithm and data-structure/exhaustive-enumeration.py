#-*- coding: UTF-8 -*-  

# exhaustive enumeration判断输入数字是否是立方数

x=int(raw_input("please enter number:"))
ans=0
while (ans**3<x):
	ans=ans+1
if ans**3==x:
	print "cube number "
else:
	print "not cube number"