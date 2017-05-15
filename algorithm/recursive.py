#-*- coding: UTF-8 -*-  

# 乘法，迭代和递归两种方式的比较
def iterMul(a, b):
	result = 0
	while b > 0:
		result += a
		b -= 1
	return result


def recurMul(a,b):
	if b==1:
		return a
	else:
		return a+recur(a,b-1)


#阶乘  迭代和递归两种方式的比较
def iterFac(n):
	res = 1
	while n > 1:
		res = res * n
		n -= 1
	return res

def recurFac(n):
	if n==1:
		return 1
	else:
		return n*recurFac(n-1)


# tower of hanoi  
def printMove(fr, to):
	print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
	if n == 1:
		printMove(fr, to)
	else:
		Towers(n-1, fr, spare, to)
		Towers(1, fr, to, spare)
		Towers(n-1, spare, to, fr)		


# 斐波那契兔子  两个base case的递归

def fib(x):
"""assumes x an int >= 0! returns Fibonacci of x"""
	assert type(x) == int and x >= 0
	if x == 0 or x == 1:
		return 1
	else:
		return fib(x-1) + fib(x-2)


# 检查是否是回文，与之前单纯数字运算不同，这里的是字符串

def isPalindrome(s):

    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans

    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPal(s[1:-1])

    return isPal(toChars(s))


# 找到列表的所有子集

def genSubsets(L):
	
	if len(L) == 0:
		return [[]]
	smaller = genSubsets(L[:-1])
	extra = L[-1:]
	new = []
	for small in smaller:
		new.append(small+extra)
	return smaller+new



