#-*- coding: UTF-8 -*-  

#二分法 找到数字的平方根，精确到0.01

x=int(raw_input("please enter number:"))
exact=0.01
high=x
low=0.0
ans=(high+low)/2.0

while abs(ans**2-x)>exact:
	if ans**2>x:
		high=ans
	else:
		low=ans
	ans=(high+low)/2.0
	print ans
print "final anwser:"+ str(ans)

