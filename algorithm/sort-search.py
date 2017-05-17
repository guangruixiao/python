
#假设列表升序排列，用二分法查找元素

def search(L, e):
	def bSearch(L, e, low, high):
		if high == low:
			return L[low] == e
		mid = low + int((high - low)/2)
		if L[mid] == e:
			return True
		if L[mid] > e:
			return bSearch(L, e, low, mid)
		else:
			return bSearch(L, e, mid + 1, high)
	if len(L) == 0:
		return False
	else:
		return bSearch(L, e, 0, len(L) - 1)


# selection-sort    复杂度：x2
def selSort(L):
	for i in range(len(L) - 1):
		minIndx = i
		minVal= L[i]
		j = i + 1
		while j < len(L):
			if minVal > L[j]:
				minIndx = j
				minVal= L[j]
			j += 1
		temp = L[i]
		L[i] = L[minIndx]
		L[minIndx] = temp


# merge-sort   复杂度：n*log(n) 
def merge(left, right, compare):
	result = []
	i,j = 0, 0
	while i < len(left) and j < len(right):
		if compare(left[i], right[j]):
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
		j += 1
	while (i < len(left)):
		result.append(left[i])
		i += 1
	while (j < len(right)):
		result.append(right[j])
		j += 1
	return result


import operator
def mergeSort(L, compare = operator.lt):
	if len(L) < 2:
		return L[:]
	else:
		middle = int(len(L)/2)
		left = mergeSort(L[:middle], compare)
		right = mergeSort(L[middle:], compare)
		return merge(left, right, compare)